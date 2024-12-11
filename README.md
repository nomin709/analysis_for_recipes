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

We are interested in investigating whether certain types of recipes, specifically those among the top 10 recipes with the fewest steps to complete, share the same average number of steps. To explore this, we use breakfast and lunch as examples and conduct a hypothesis test to determine if the average number of steps for breakfast recipes is the same as that for lunch recipes.

**Null Hypothesis:** The average number of steps for breakfast recipes is equal to the average number of steps for lunch recipes. 

**Alternative Hypothesis:**  The average number of steps for breakfast recipes is different than the average number of steps for lunch recipes. 

**Test Statistics:** We plan to use permutation testing with the absolute difference between the means of breakfast recipes and lunch recipes as the test statistic.

**Significance Level:** 0.05

- Distribution of Numer of Steps for Breakfast and Lunch Recipes

<iframe
  src="assets/hypo.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

We conducted a permutation test by randomly shuffling the tags for "breakfast" and "lunch" and reassigning them to a new column called 'breakfast_lunch'. This process was repeated 1,000 times. For each iteration, we calculated the absolute difference in the mean number of steps between the shuffled groups, resulting in a distribution of 1,000 simulated statistics.

<iframe
  src="assets/emp_hypo.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

The observed absolute difference in means from the dataset is 0.38, represented by a red line on the empirical histogram. The line is positioned far to the right of the simulated distribution, indicating a significant deviation. The p-value of the observed statistic is 0.0, suggesting it is highly unlikely that the average number of steps for breakfast recipes is the same as for lunch recipes. Therefore, we reject the null hypothesis that the average number of steps for breakfast is equal to the average number of steps for lunch. 
It is important to note that the hypothesis test is based solely on the provided dataset and does not definitively prove that the average number of steps for breakfast is always different from that for lunch. The observed difference in average steps could be influenced by the general perception that breakfast is often treated as a simpler meal compared to lunch, which might explain the disparity in the average number of steps. 

## Framing a Prediction Problem

We aim to predict the number of steps (`n_steps`) in recipes, which is a regression problem. The target variable (`n_steps`) is quantitative and continuous, making regression the appropriate modeling approach.

The response variable we are predicting is the number of steps (`n_steps`) in a recipe. We chose this variable because it effectively reflects the numerical value of steps in a recipe within the dataset.

To evaluate our model, we will use Root Mean Squared Error (RMSE) instead of the Coefficient of Determination (R-squared). RMSE provides a more direct and interpretable measure of prediction accuracy by indicating the average error in the same units as the response variable. While R-squared measures how well the model explains the variance in the data, RMSE offers a clearer understanding of the actual prediction errors, making it a more practical metric for our model's performance evaluation. It helps us determine how many steps our prediction values deviate from the actual number, on average.

In our previous analysis, we identified an increasing trend between the number of steps (`n_steps`) and the number of ingredients (n_ingredients), which could be useful in predicting the number of steps. Additionally, there is a significant difference between the average number of steps for breakfast and lunch recipes as determined in the Hypothesis Testing section, suggesting that tags could be valuable in our prediction model.

At the time of the prediction, we know the following information:
- Preparation time (`minutes`): Available before the recipe steps are known.
- Number of ingredients (`n_ingredients`): Also known before determining the steps.
- Tags (`tags`): These categorical labels can provide contextual information about the recipe type.
- Average rating (`rating_avg`): Known from user feedback or historical data.

This information allows us to predict the number of steps required for recipes based on features available at the prediction time, ensuring that our model is trained and evaluated in a way that is both realistic and practical.

## Baseline Model

For our baseline model, we are using a random forest regressor because it seems that predictor variables and explanotory variables have no clear linear relationship thus random forest regressor may be better at handling complex interactions and non-linear patterns. We are predicting number of steps (`n_steps`) based on the features: preparation time (`minutes`) and number of ingredients (`n_ingredients`).

`n_steps` and `n_ingredients` are variables containing quantitative numerical values. Therefore, we leave them as-is and build random forest regressor using these features with a `max_depth` of 5. 

To evaluate our model performance, we split the data into training and test sets, and fit the model on the training dataset. We then evaluated model performance on train and test sets. This baseline model didn't perform well because 

Train RMSE: 5.509
Test RMSE: 5.521

## Final Model

State the features you added and why they are good for the data and prediction task. Note that you can’t simply state “these features improved my accuracy”, since you’d need to choose these features and fit a model before noticing that – instead, talk about why you believe these features improved your model’s performance from the perspective of the data generating process.

Describe the modeling algorithm you chose, the hyperparameters that ended up performing the best, and the method you used to select hyperparameters and your overall model. Describe how your Final Model’s performance is an improvement over your Baseline Model’s performance.

Our final model uses the following features: `n_ingredients`, `minutes`, `tags`, `rating_avg`.

To improve the model, we would look into tags and take specific tags as indicators to predict the number of steps.

I used GridSearchCV to find the best hyperparameters for the RandomForestRegressor.
The best hyperparameters are:
- max_depth: 30
- n_estimators: 150
- min_samples_split: 3

Train RMSE (Best Model): 3.2974
Test RMSE (Best Model): 3.9237

The final model performed better than the baseline model, as indicated by the increase in RMSE score for the final model comapred to our initial baseline model.

## Fairness Analysis

For the fairness analysis, we will assess if our final model is fair among recipes with lower average ratings and high average ratings. We are trying to determine if our model perform worse for low rated recipes than it does for high rated recipes. To evaluate this, we performed a permutation test and examined the result of the difference in RMSE between the two groups. 

To run the permutation test, we created a new column `low_rating` that indicates whether a recipe is low rated or high rated. We categorized the recipes by their average rating with a threshold of 4 where recipes with average rating less than 4 is classified as low rated, and if the average rating is greater than or equal to 4, recipe is classified as high rated.

**Null Hypothesis:** Our model is fair. Its RMSE for low rated recipes and high rated recipes are roughly the same, and any differences are due to random chance.

**Alternative Hypothesis:** Our model is unfair. Its RMSE for low rated recipes is lower than its RMSE for high rated recipes.

**Test Statistics:**  Absolute difference in RMSE scores (low rated recipes - high rated recipes)

**Significance Level:** 0.05

<iframe
  src='assets/fairness_emp.html'
  width="800"
  height="600"
  frameborder="0"
></iframe>

After performing the permutation test with 1000 trails, we calculated a p-value of 0.379, which is greater than the significance level of 0.05. Therefore, we fail to reject the null hypothesis that our mode is fair, indicating that the RMSE for low rated recipes and high rated recipes are roughly the same, and any differences are due to random chance. This implies that our model predicts recipes from both groups with statistically similar errors which suggests our model is relatively fair and doesn't perform in favor of either low-rated recipes or high-rated recipes.