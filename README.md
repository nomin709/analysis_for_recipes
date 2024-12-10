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

7. Drop columns containing text data.
- Since the analysis focuses on types of recipes and the number of steps, we drop columns containing text like 'steps,' 'description,' and 'review' to enhance the dataset's clarity.

##### Clean DataFrame

<div style="max-height: 400px; overflow-y: scroll;">
| name                                 |     id |   minutes |   contributor_id | submitted   | tags                                                                                                                                                                                                                        | nutrition                                    |   n_steps | ingredients                                                                                                                                                                    |   n_ingredients |   user_id |   recipe_id | date       |   rating |   rating_avg |
|:-------------------------------------|-------:|----------:|-----------------:|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------|----------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------:|----------:|------------:|:-----------|---------:|-------------:|
| 1 brownies in the world    best ever | 333281 |        40 |           985201 | 2008-10-27  | ['60-minutes-or-less', 'time-to-make', 'course', 'main-ingredient', 'preparation', 'for-large-groups', 'desserts', 'lunch', 'snacks', 'cookies-and-brownies', 'chocolate', 'bar-cookies', 'brownies', 'number-of-servings'] | [138.4, 10.0, 50.0, 3.0, 3.0, 19.0, 6.0]     |        10 | ['bittersweet chocolate', 'unsalted butter', 'eggs', 'granulated sugar', 'unsweetened cocoa powder', 'vanilla extract', 'brewed espresso', 'kosher salt', 'all-purpose flour'] |               9 |    386585 |      333281 | 2008-11-19 |        4 |            4 |
| 1 in canada chocolate chip cookies   | 453467 |        45 |          1848091 | 2011-04-11  | ['60-minutes-or-less', 'time-to-make', 'cuisine', 'preparation', 'north-american', 'for-large-groups', 'canadian', 'british-columbian', 'number-of-servings']                                                               | [595.1, 46.0, 211.0, 22.0, 13.0, 51.0, 26.0] |        12 | ['white sugar', 'brown sugar', 'salt', 'margarine', 'eggs', 'vanilla', 'water', 'all-purpose flour', 'whole wheat flour', 'baking soda', 'chocolate chips']                    |              11 |    424680 |      453467 | 2012-01-26 |        5 |            5 |
| 412 broccoli casserole               | 306168 |        40 |            50969 | 2008-05-30  | ['60-minutes-or-less', 'time-to-make', 'course', 'main-ingredient', 'preparation', 'side-dishes', 'vegetables', 'easy', 'beginner-cook', 'broccoli']                                                                        | [194.8, 20.0, 6.0, 32.0, 22.0, 36.0, 3.0]    |         6 | ['frozen broccoli cuts', 'cream of chicken soup', 'sharp cheddar cheese', 'garlic powder', 'ground black pepper', 'salt', 'milk', 'soy sauce', 'french-fried onions']          |               9 |     29782 |      306168 | 2008-12-31 |        5 |            5 |
| 412 broccoli casserole               | 306168 |        40 |            50969 | 2008-05-30  | ['60-minutes-or-less', 'time-to-make', 'course', 'main-ingredient', 'preparation', 'side-dishes', 'vegetables', 'easy', 'beginner-cook', 'broccoli']                                                                        | [194.8, 20.0, 6.0, 32.0, 22.0, 36.0, 3.0]    |         6 | ['frozen broccoli cuts', 'cream of chicken soup', 'sharp cheddar cheese', 'garlic powder', 'ground black pepper', 'salt', 'milk', 'soy sauce', 'french-fried onions']          |               9 |   1196280 |      306168 | 2009-04-13 |        5 |            5 |
| 412 broccoli casserole               | 306168 |        40 |            50969 | 2008-05-30  | ['60-minutes-or-less', 'time-to-make', 'course', 'main-ingredient', 'preparation', 'side-dishes', 'vegetables', 'easy', 'beginner-cook', 'broccoli']                                                                        | [194.8, 20.0, 6.0, 32.0, 22.0, 36.0, 3.0]    |         6 | ['frozen broccoli cuts', 'cream of chicken soup', 'sharp cheddar cheese', 'garlic powder', 'ground black pepper', 'salt', 'milk', 'soy sauce', 'french-fried onions']          |               9 |    768828 |      306168 | 2013-08-02 |        5 |            5 |
</div>

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
