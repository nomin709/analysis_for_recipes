"""
Imports and helpful functions that we use in DSC 80 lectures. Use `make
setup-lec` to copy this (and custom-rise-styles.css) to the lecture folders.

Usage:

from dsc80_utils import *
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_inline.backend_inline import set_matplotlib_formats
from IPython.display import display, IFrame, HTML

import plotly
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "notebook"

# DSC 80 preferred styles
pio.templates["dsc80"] = go.layout.Template(
    layout=dict(
        margin=dict(l=30, r=30, t=30, b=30),
        autosize=True,
        width=600,
        height=400,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        title=dict(x=0.5, xanchor="center"),
    )
)
pio.templates.default = "simple_white+dsc80"

set_matplotlib_formats("svg")
sns.set_context("poster")
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# display options for numpy and pandas
np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

# Use plotly as default plotting engine
pd.options.plotting.backend = "plotly"


def display_df(
    df, rows=pd.options.display.max_rows, cols=pd.options.display.max_columns
):
    """Displays n rows and cols from df"""
    with pd.option_context(
        "display.max_rows", rows, "display.max_columns", cols
    ):
        display(df)


def dfs_side_by_side(*dfs):
    """
    Displays two or more dataframes side by side.
    """
    display(
        HTML(
            f"""
        <div style="display: flex; gap: 1rem;">
        {''.join(df.to_html() for df in dfs)}
        </div>
    """
        )
    )

from pathlib import Path

# The stuff below is for Lecture 7/8.
def create_kde_plotly(df, group_col, group1, group2, vals_col, title=''):
    fig = ff.create_distplot(
        hist_data=[df.loc[df[group_col] == group1, vals_col], df.loc[df[group_col] == group2, vals_col]],
        group_labels=[group1, group2],
        show_rug=False, show_hist=False
    )
    return fig.update_layout(title=title)

def multiple_hists(df_map, histnorm="probability", title=""):
    values = [df_map[df_name]["child"].dropna() for df_name in df_map]
    all_sets = pd.concat(values, keys=list(df_map.keys()))
    all_sets = all_sets.reset_index()[["level_0", "child"]].rename(
        columns={"level_0": "dataset"}
    )
    fig = px.histogram(
        all_sets,
        color="dataset",
        x="child",
        barmode="overlay",
        histnorm=histnorm,
    )
    fig.update_layout(title=title)
    return fig


def multiple_kdes(df_map, title=""):
    values = [df_map[key]["child"].dropna() for key in df_map]
    labels = list(df_map.keys())
    fig = ff.create_distplot(
        hist_data=values,
        group_labels=labels,
        show_rug=False,
        show_hist=False,
        colors=px.colors.qualitative.Dark2[: len(df_map)],
    )
    return fig.update_layout(title=title).update_xaxes(title="child")

def multiple_describe(df_map):
    out = pd.DataFrame(
        columns=["Dataset", "Mean", "Standard Deviation"]
    ).set_index("Dataset")
    for key in df_map:
        out.loc[key] = df_map[key]["child"].apply(["mean", "std"]).to_numpy()
    return out

def make_mcar(data, col, pct=0.5):
    """Create MCAR from complete data"""
    missing = data.copy()
    idx = data.sample(frac=pct, replace=False).index
    missing.loc[idx, col] = np.NaN
    return missing


def make_mar_on_cat(data, col, dep_col, pct=0.5):
    """Create MAR from complete data. The dependency is
    created on dep_col, which is assumed to be categorical.
    This is only *one* of many ways to create MAR data.
    For the lecture examples only."""

    missing = data.copy()
    # pick one value to blank out a lot
    high_val = np.random.choice(missing[dep_col].unique())
    weights = missing[dep_col].apply(lambda x: 0.9 if x == high_val else 0.1)
    idx = data.sample(frac=pct, replace=False, weights=weights).index
    missing.loc[idx, col] = np.NaN

    return missing


def make_mar_on_num(data, col, dep_col, pct=0.5):
    """Create MAR from complete data. The dependency is
    created on dep_col, which is assumed to be numeric.
    This is only *one* of many ways to create MAR data.
    For the lecture examples only."""

    thresh = np.percentile(data[dep_col], 50)

    def blank_above_middle(val):
        if val >= thresh:
            return 0.75
        else:
            return 0.25

    missing = data.copy()
    weights = missing[dep_col].apply(blank_above_middle)
    idx = missing.sample(frac=pct, replace=False, weights=weights).index

    missing.loc[idx, col] = np.NaN
    return missing

def permutation_test(data, col, group_col, test_statistic, N=1000):
    """
    Conduct a permutation test to compare two groups based on a given test
    statistic.

    This function computes the observed test statistic for the two groups in the
    dataset, and then generates a distribution of permuted test statistics by
    repeatedly shuffling the group labels and calculating the test statistic on
    the shuffled data. The result is a distribution of permuted statistics and
    the observed statistic for comparison.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame containing the data to be tested, along with the
        group labels.
    col : str
        The name of the column in `data` that contains the data values to be
        compared between the two groups.
    group_col : str
        The name of the column in `data` that contains the group labels. There
        should be exactly two unique groups in this column.
    test_statistic : function
        A function that calculates the test statistic based on the data column
        and the group column. This function must accept three arguments: the
        data DataFrame, the name of the data column, and the name of the group
        column.
    N : int, optional (default=1000)
        The number of permutations to perform in the test.

    Returns
    -------
    shuffled_stats : np.ndarray
        An array of test statistics computed from the permuted datasets.
    obs : np.floating
        The observed test statistic calculated from the original data.
    """
    obs = test_statistic(data, col, group_col)
    shuffled = data.copy()

    shuffled_stats = []
    for _ in range(N):
        shuffled[col] = np.random.permutation(shuffled[col])
        shuffled_stat = test_statistic(shuffled, col, group_col)
        shuffled_stats.append(shuffled_stat)

    shuffled_stats = np.array(shuffled_stats)

    return shuffled_stats, obs


def abs_diff_in_means(data, col, group_col):
    """
    Compute the difference in means between two groups.

    This function calculates the difference in means of the values in the
    specified column between two groups defined by the group column.

    Parameters
    ----------
    data : pandas.DataFrame
        The input DataFrame containing the data and group labels.
    col : str
        The name of the column in `data` that contains the numeric data for
        which the mean will be computed.
    group_col : str
        The name of the column in `data` that contains the group labels. There
        should be exactly two unique groups in this column.

    Returns
    -------
    float
        The difference in means between the two groups. The result is
        calculated as mean(group2) - mean(group1), where the group ordering is
        based on their appearance in the DataFrame.
    """
    return abs(data.groupby(group_col)[col].mean().diff().iloc[-1])