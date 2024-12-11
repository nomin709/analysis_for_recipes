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

1. Left merge the recipes and interactions datasets together.
- The reviews and ratings in the interactions dataset will match the corresponding recipes in the recipes dataset. For recipes that do not appear in the interactions dataset, the reviews, ratings, and merged columns will be null. 

2. Fill all ratings of 0 with np.nan in the merged dataset. 
- Filling ratings of 0 with np.nan helps represent missing values, preventing potential bias in the analysis.

3. Add a column containing the average rating for each recipe.
- The average rating for each recipe provides a good indicator of the overall user reviews for that recipe.

4. Convert the values in the 'tags' column from strings to lists.
- Converting the values into lists allows us to identify and extract individual tags, which is useful for categorizing recipes by type.

5. Convert the values in the 'user_id' column from float to integer.
- We convert the values in the 'user_id' column for better representation.

6. Convert the values in the 'recipe_id' column from float to integer.
- We convert the values in the 'recipe_id' column for better representation. 

7. Drop 'step' column.
- Since the analysis focuses on types of recipes and the number of steps, we drop column containing text like 'steps' to enhance the dataset's clarity.

##### Clean DataFrame

<iframe src="assets/dataframe.html" style="width: 100%; height: 400px; border: none; overflow: auto;"></iframe>

#### Univariate Analysis

We examined the distribution of n_steps and found no missing values in the column. The distribution appears to be right-skewed, with most recipes requiring fewer than 20 steps. Upon analyzing the statistics, we found that the mean number of steps is approximately 10, the median is 9, the maximum is 100, and the minimum is 1. 

<iframe
  src="assets/univariate.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

#### Bivariate Analysis

We examined the distribution of n_ingredients and found no missing values in the column. The plot shows that the number of ingredients mostly ranges from 0 to 30, with the majority falling within 40 steps.

<iframe
  src="assets/bivariate.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

#### Interesting Aggregates

| tags       |        1 |       2 |       3 |
|:-----------|---------:|--------:|--------:|
| american   |  18.8945 | 59.9345 | 40.8085 |
| appetizers |  12.4509 | 41.2602 | 36.2605 |
| breakfast  |  36.7671 | 18.0526 | 30.2157 |
| brunch     | 100.421  | 10.2177 | 31.021  |
| desserts   |  15.2672 | 20.0771 | 38.6757 |
| european   |  46.2705 | 25.7961 | 37.1663 |
| fruit      |  30.574  | 14.4203 | 25.3304 |
| lunch      |  52.9877 | 17.5945 | 34.9934 |
| salads     |  24.5385 | 17.5127 | 23.2074 |
| vegetarian |  10.7028 | 23.1497 | 25.9033 |

We aim to investigate which types of recipes tend to be more efficient by focusing on those with fewer steps. To do this, we set a threshold of steps to 3 or fewer, creating a query DataFrame of such recipes. Since each recipe can have multiple tags, we explode the tags column and count the frequency of each tag to identify the top 30 most common ones. Tags often describe characteristics of a recipe rather than its type, so we manually filtered the top 10 tags based on our judgment. Note that because recipes can have multiple tags, the resulting data contains repeated entries. However, our goal is to identify overall patterns.
The pivot table above shows the mean preparation time (in minutes) for each number of steps, based on the top 10 tags we selected. From the table, we observe that the mean preparation time varies by recipe type and step count, likely influenced by outliers—individual recipes that require significantly more time. Despite these variations, many recipe types have a mean preparation time within 20 minutes. This insight provides a useful guide for college students seeking quick and efficient meal options.

## Assessment of Missingness

In the merged dataset, we observe that the columns with the most significant number of missing values are rating, rating_avg, and description.

#### NMAR Analysis

We believe the missingness in the description column is Not Missing at Random (NMAR). Since recipes are user-generated, it is likely optional for users to include a description when uploading their recipes to the platform. Some users may choose not to write a description because it takes time, while others may feel that the description does not add value in explaining the recipe's complexity. Additionally, some users might omit the description because the recipes are simple and self-explanatory, making a description unnecessary.

#### Missingness Dependency

We aim to investigate whether the missingness of the rating column depends on n_steps and minutes.

***Rating Vs. Number of Steps***

**Null Hypothesis:** The missingness of rating does not depend on n_steps.

**Alternative Hypothesis:** The missingness of rating does depend on number of steps.

**Test Statistics:** After comparing the distributions of the number of steps for cases where the rating is missing and not missing, we found that the distributions have similar centers but different shapes. As a result, we decided to use the K-S statistic as our test statistic.

**Significance Level:** 0.05

<iframe
  src="assets/mar_dist.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

We can see that the distributions center roughly the same place but have different shapes.

We performed a permutation test by shuffling n_steps 1,000 times and collecting the K-S statistic for each of the 1,000 simulated samples to obtain the distribution of simulated statistics.

<iframe
  src="assets/mar_emp.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

The observed statistic for the given data is 0.067, represented by the red vertical line on the histogram plot. The p-value of this observed statistic is 0.0, which is less than the significance level of 0.05. Therefore, we reject the null hypothesis that the missingness of the rating does not depend on the number of steps.

***Rating Vs. Minutes***

**Null Hypothesis:** The missingness of rating does not depend on minutes.

**Alternative Hypothesis:** The missingness of rating does depend on minutes.

**Test Statistics:** We use the absolute difference of means as the test statistic to evaluate how the observed value compares to the empirical distribution generated under the null hypothesis.

**Significance Level:** 0.05

<iframe
  src="assets/mcar_dist.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

We observe that there are outliers in the "minutes" column, with some recipes taking over 1 million minutes to prepare. To improve the visualization and better understand the distribution between ratings that are missing and those that are not, we remove potential outliers by eliminating recipes with more than 4000 minutes of preparation time. This allows for a clearer distribution and better visualization of the data.

<iframe
  src="assets/mcar_dist_2.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

<iframe
  src="assets/mcar_emp.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

We performed a permutation test on the dataset and collected the sample statistics. The observed test statistic is 51.45, represented by the red line in the empirical distribution. Some sample statistics exceed the observed value. The p-value of 0.105 is greater than the significance level of 0.05. Therefore, we fail to reject the null hypothesis that the rating does not depend on minutes.

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
