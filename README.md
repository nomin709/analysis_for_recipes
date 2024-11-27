# Analysis For Recipes

by Nomin Batjargal and An-Chi Lu

## Introduction

Question: What types of recipes tend to have lower number of steps (the least number of steps)?

## Data Cleaning and Exploratory Data Analysis

#### Cleaning

#### Univariate Analysis

#### Bivariate Analysis

#### Interesting Aggregates

## Assessment of Missingness

#### NMAR Analysis

#### Missingness Dependency

## Hypothesis Testing

**Null Hypothesis:** The average number of steps for breakfast recipes is equal to the average number of steps for lunch recipes

**Alternative Hypothesis:** The average number of steps for breakfast recipes is different than the average number of steps for lunch recipes

**Test Statistics:** Permutation testing using the absolute difference between the means of breakfast recipes and lunch recipes

**Significance Level:** 0.01

## Framing a Prediction Problem

Prediction Problem: Predicting number of steps, regression/classification problem
Response variable: number of step (n_steps)
Features: preparation time in min (minutes), number of ingredients (n_ingredients), tags

## Baseline Model

Predicting number of steps based on minutes (numerical) and number of ingredient (numerical).
- all steps (feature transforms and model training) in a single sklearn Pipeline
- take care of categorical columns using appropriate encoding

## Final Model

To improve the model, we would look into tags and take specific tags as indicators to predict the number of steps.

## Fairness Analysis