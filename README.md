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

For our baseline model, we chose a Random Forest Regressor due to the lack of a clear linear relationship between the predictor variables and the target variable. The Random Forest Regressor is well-suited to handle complex interactions and non-linear patterns. 

We are predicting the number of steps (`n_steps`) based on the following features: 

- preparation time (`minutes`): We believe it is likely to influence the number of steps (`n_steps`) in a recipe

- number of ingredients (`n_ingredients`): It may impact the number of steps (`n_steps`), as more ingredients may require more steps to prepare and combine.

Both `minutes` and `n_ingredients` are quantitative numerical values, so we included them as-is in our model. We built the Random Forest Regressor with a max_depth of 5.

To evaluate our model performance, we split the data into training and test sets. We fit the model on the training dataset and then evaluated its performance on both the train and test sets. The results are as follows:

Train RMSE: 5.51

Test RMSE: 5.52

The close values of train and test RMSE suggest that there is no overfitting. However, the maximum n_steps in the dataset is 100, and an RMSE of 5.52 indicates that, on average, the model's predictions are off by about 5.52 steps. Given that the mean number of steps (`n_steps`) is 10, this error seems significant. Less RMSE is good as it implies a small error, however the test RMSE for our baseline model seems relatively high.

Only using `minutes` and `n_ingredients` may not provide enough information for the model to accurately predict the number of steps, leading to suboptimal performance. The relationship between the number of steps and the provided features might be influenced by other factors that are not captured by these two variables alone, such as recipe complexity or specific ingredient types. The chosen max_depth of 5 might be limiting the model's ability to fully capture the intricacies of the data.

To improve the model's performance, we could consider incorporating additional relevant features, tuning the hyperparameters further, and transforming certain columns.

## Final Model

In this section, we will add more features and transform certain columns, as well as tune the hyperparameters further in Random Forest Regressor toimprove our model's performance.

Our final model uses the following features: `n_ingredients`, `minutes`, `tags`, `rating_avg`.

On top of `n_ingredients` and `minutes` that we used for baseline model, we added two more features from the data, `tags` and `rating_avg`.

`n_ingredients`

As mentioned, we believe that number of ingredients may impact the number of steps (`n_steps`), as more ingredients may require more steps to prepare and combine. We also noted that there is a slight increasing pattern between `n_steps` and `n_ingredients` from the scatterplot we plotted. Although, the pattern doesn't seem to be signifanct to infer a clear relationship between them, this trend might be useful in helping the model predict the number of steps. This column is numerical so we left it as is in our final model.

`minutes`

This column represents the preparation time in minutes. We suspect there might be a pattern between `n_steps` and `minutes` because we believe that with more preparation or cooking time, it is highly likely that number of steps would be high, because more time means more things to do, most of the times although there might exceptions. We observed that the distribution of `minutes` is highly right skewed so we log transformed it to normalize.

`tags`

To improve the model, we look into `tags` and take specific tags as indicators to predict the number of steps. Because there are 549 unque tags, we chose 9 relevant tags that we deemed important and significant in recipes to reduce complexity. The selected tags are:
breakfast, lunch, dinner, snacks, desserts, beverages, appetizers, vegetarian, side-dishes. Then we manually one hot encoded each recipe using these tags, applying 1 if a recipe has the tag and 0 if not, for each of these selected tags.

`rating_avg`

There wasn't a clear pattern between `n_steps` and `rating_avg` which may be due to its large variability in the data but also np correlation between the variables. However, we believe that the average rating of a recipe may play a role in predicting number of steps because somee recipes with less steps may tend to have higher rating for its simplicity and efficiency in cooking. This column is continious numerical, as it takes the average rating of recipes, so we left it as is in our final model.

After preprocessing the columns, I used GridSearchCV to find the best hyperparameters for the RandomForestRegressor.

We tested different values in three hyperparameters and the value as follows:

- `max_depth`: [5, 10, 20, 30],
- `n_estimators`: [50, 100, 150],
- `min_samples_split`: [2, 3, 4, 5]

GridSearchCV results show that the best hyperparameters are:
- max_depth: 30
- n_estimators: 150
- min_samples_split: 3

We evaluated the final model performance using the same training and testing sets. The results are as follows:

Train RMSE (Best Model): 3.32

Test RMSE (Best Model): 3.93

The final model performed better than the baseline model, as indicated by the decrease in RMSE score for the final model compared to our initial baseline model. The test RMSE decreased from 5.52 to 3.93, which is a good improvement.

## Fairness Analysis

We will perform a fairness analysis to determine if our final model is fair in predicting the number of steps (`n_steps`) for recipes with low average ratings compared to those with high average ratings. Specifically, we aim to assess whether the model performs worse for low-rated recipes than for high-rated recipes. For this analysis, we will conduct a permutation test and examine the difference in RMSE between the two groups.

**Null Hypothesis:** Our model is fair. Its RMSE for low-rated and high-rated recipes are roughly the same, with any differences being due to random chance.

**Alternative Hypothesis:** Our model is unfair. Its RMSE for low-rated recipes is lower than its RMSE for high-rated recipes.

**Test Statistics:**  Difference in RMSE between low-rated and high-rated recipes (low rated recipes - high rated recipes)

**Significance Level:** 0.05

To run the permutation test, we created a new column `low_rating` to classify recipes based on their average ratings. Recipes with an average rating of less than 4 were classified as low-rated, and those with an average rating of 4 or higher were classified as high-rated. We then shuffle the `low_rating` column for 1000 times to collect 1000 simulating differences in the two distributions as described in the test statistic.

<iframe
  src='assets/fairness_emp.html'
  width="800"
  height="600"
  frameborder="0"
></iframe>

After performing the permutation test, we got an observed test statistic of -0.41 and a p-value of 0.99, which is greater than the significance level of 0.05. Therefore, we fail reject the null hypothesis that our mode is fair, indicating that the model's RMSE for low-rated and high-rated recipes are roughly the same, with any differences being due to random chance. This finding suggests that our model is relatively fair and tends to perform similarly across the two groups. Hence, it doesn't show a significant bias in favor of either low-rated or high-rated recipes. We can consider the model's predictions to be equitable across these categories, based on the current analysis.