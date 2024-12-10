# Exploring Recipe Types with Fewer Steps: An Analysis of Simplicity and Efficiency in Cooking

by Nomin Batjargal and An-Chi Lu

## Introduction

As we enter college, the pace of life becomes faster and more stressful compared to high school. Balancing assignments, projects, and deadlines often feels like a race against time. During exam weeks, some students might even skip meals to focus on studying. For many of us, cooking our own meals is a normal part of college life. However, during such time-constrained periods, we often look for ways to prepare food quickly while still satisfying our hunger.
**This need for efficiency has led us to explore what types of recipes tend to require fewer steps, making them quicker to prepare.** To investigate, we are analyzing two datasets from Food.com, an online platform where users upload and share recipes. These datasets, scraped from the website, provide detailed information on recipe steps, allowing us to identify trends in simpler, time-saving meals.

The first dataset, recipes, contains 83,782 rows and 12 columns. Below is a description of each column in the dataset: 

| Column   | Description    |
|-------------|-------------|
| name | Recipe name|
| id | Recipe ID | 
| minutes | Minutes to prepare recipe |
| contributor_id | User ID who submitted this recipe | 
| submitted | Date recipe was submitted |
| tags | Food.com tags for recipe | 
| nutrition | Nutrition information in the form [calories (#), total fat (PDV), sugar (PDV), sodium (PDV), protein (PDV), saturated fat (PDV), carbohydrates (PDV)]; PDV stands for “percentage of daily value” |
| n_steps | Number of steps in recipe | 
| steps | Text for recipe steps, in order |
| description | User-provided description | 
| ingredients | Recipe ingredients |
| n_ingredients | Number of ingredients in recipe | 


The second dataset, interactions, consists of 731,927 rows and 5 columns. This dataset captures user reviews and ratings for the recipes, providing insights into how users interact with and evaluate the recipes. The description of each column is shown below:

| Column   | Description    |
|-------------|-------------|
| user_id | User ID |
| recipe_id | Recipe ID | 
| date | Date of interaction |
| rating | Rating given | 
| review | Review text |

To explore **which types of recipes tend to have a lower number of steps**, we will focus specifically on the n_steps and tags columns in the dataset. To enhance the quality of our analysis, we will begin with data cleaning. This involves merging the two datasets into a single dataset, adjusting data types, and making any necessary modifications to the columns for consistency and clarity.

## Data Cleaning and Exploratory Data Analysis

#### Data Cleaning

Describe, in detail, the data cleaning steps you took and how they affected your analyses. The steps should be explained in reference to the data generating process. Show the head of your cleaned DataFrame 

#### Univariate Analysis

Embed at least one plotly plot you created in your notebook that displays the distribution of a single column (see Part 2: Report for instructions). Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present. (Your notebook will likely have more visualizations than your website, and that’s fine. Feel free to embed more than one univariate visualization in your website if you’d like, but make sure that each embedded plot is accompanied by a description.)

#### Bivariate Analysis

Embed at least one plotly plot that displays the relationship between two columns. Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present. (Your notebook will likely have more visualizations than your website, and that’s fine. Feel free to embed more than one bivariate visualization in your website if you’d like, but make sure that each embedded plot is accompanied by a description.)

#### Interesting Aggregates

Embed at least one grouped table or pivot table in your website and explain its significance.

## Assessment of Missingness

#### NMAR Analysis

Recall, to determine whether data are likely NMAR, you must reason about the data generating process; you cannot conclude that data are likely NMAR solely by looking at your data. As such, there’s no code to write here (and hence, nothing to put in your notebook).

State whether you believe there is a column in your dataset that is NMAR. Explain your reasoning and any additional data you might want to obtain that could explain the missingness (thereby making it MAR). Make sure to explicitly use the term “NMAR.”

#### Missingness Dependency

Present and interpret the results of your missingness permutation tests with respect to your data and question. Embed a plotly plot related to your missingness exploration; ideas include:

• The distribution of column Y when column X is missing and the distribution of column Y when column X is not missing, as was done in Lecture 8.

• The empirical distribution of the test statistic used in one of your permutation tests, along with the observed statistic.

missingness of: n_steps

column does depend on: minutes, n_ingredients, rating, contributor_id, submitted


**Null Hypothesis:** The missingness of rating does not depend on n_steps.
(Distribution of league when firstblood is missing is the same as the distribution of league when firstblood is not missing.)
(if we fail to reject the null that the distribution of the column when 'child' is missing is the same as the distribution of the column when 'child' is not missing, then we can conclude 'child' is MCAR.)

**Alternative Hypothesis:** The missingness of number of steps does depend on ''.

**Test Statistics:** The absolute difference of mean in the '' of the distribution of the group with missing number of steps and the distribution of the group without missing number of steps.
(diif in means, tvd, ks)
Strategy: Always plot the two distributions you are comparing.
- If the distributions have similar shapes but are centered in different places, use the difference in means (or absolute difference in means).
- If your alternative hypothesis involves a "direction" (i.e. smoking weights were are on average than non-smoking weights), use the difference in means.
- If the distributions have different shapes but roughly the same center, and your alternative hypothesis is simply that the two distributions are different, use the K-S statistic.

**Significance Level:** 0.05

missingness of: n_steps

column does not depend on: id, name, nutrition, user_id

**Null Hypothesis:** The missingness of number of steps does not depend on ''.

**Alternative Hypothesis:** The missingness of number of steps does depend on ''.

**Test Statistics:** The absolute difference of mean in the '' of the distribution of the group with missing number of steps and the distribution of the group without missing number of steps.

**Significance Level:** 0.05

## Hypothesis Testing

Clearly state your null and alternative hypotheses, your choice of test statistic and significance level, the resulting 
p-value, and your conclusion. Justify why these choices are good choices for answering the question you are trying to answer.

Optional: Embed a visualization related to your hypothesis test in your website.

Tip: When making writing your conclusions to the statistical tests in this project, never use language that implies an absolute conclusion; since we are performing statistical tests and not randomized controlled trials, we cannot prove that either hypothesis is 100% true or false.

**Null Hypothesis:** The average number of steps for breakfast recipes is equal to the average number of steps for lunch recipes

**Alternative Hypothesis:** The average number of steps for breakfast recipes is different than the average number of steps for lunch recipes

**Test Statistics:** Permutation testing using the absolute difference between the means of breakfast recipes and lunch recipes

**Significance Level:** 0.05

## Framing a Prediction Problem

Clearly state your prediction problem and type (classification or regression). If you are building a classifier, make sure to state whether you are performing binary classification or multiclass classification. Report the response variable (i.e. the variable you are predicting) and why you chose it, the metric you are using to evaluate your model and why you chose it over other suitable metrics (e.g. accuracy vs. F1-score).

Note: Make sure to justify what information you would know at the “time of prediction” and to only train your model using those features. For instance, if we wanted to predict your final exam grade, we couldn’t use your Final Project grade, because the project is only due after the final exam! Feel free to ask questions if you’re not sure.

Prediction Problem: Predicting number of steps, regression/classification problem
Response variable: number of step (n_steps)
Features: preparation time in min (minutes), number of ingredients (n_ingredients), tags, rating, contributor_id

## Baseline Model

Describe your model and state the features in your model, including how many are quantitative, ordinal, and nominal, and how you performed any necessary encodings. Report the performance of your model and whether or not you believe your current model is “good” and why.

Tip: Make sure to hit all of the points above: many projects in the past have lost points for not doing so.

Predicting number of steps based on minutes (numerical) and number of ingredient (numerical).
- all steps (feature transforms and model training) in a single sklearn Pipeline
- take care of categorical columns using appropriate encoding

## Final Model

State the features you added and why they are good for the data and prediction task. Note that you can’t simply state “these features improved my accuracy”, since you’d need to choose these features and fit a model before noticing that – instead, talk about why you believe these features improved your model’s performance from the perspective of the data generating process.

Describe the modeling algorithm you chose, the hyperparameters that ended up performing the best, and the method you used to select hyperparameters and your overall model. Describe how your Final Model’s performance is an improvement over your Baseline Model’s performance.

Optional: Include a visualization that describes your model’s performance, e.g. a confusion matrix, if applicable.

To improve the model, we would look into tags and take specific tags as indicators to predict the number of steps.

## Fairness Analysis

Clearly state your choice of Group X and Group Y, your evaluation metric, your null and alternative hypotheses, your choice of test statistic and significance level, the resulting 
p-value, and your conclusion.

Optional: Embed a visualization related to your permutation test in your website.

Does my model perform worse for individuals in Group X than it does for individuals in Group Y?”, for an interesting choice of X and Y ?

Permutation Test

**Null Hypothesis:** Our model is fair. Its precision for young people and old people are roughly the same, and any differences are due to random chance.

**Alternative Hypothesis:** Our model is unfair. Its precision for young people is lower than its precision for old people.

**Test Statistics:** 

**Significance Level:** 0.05
