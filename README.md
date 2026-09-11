# Exploring Recipe Types with Fewer Steps: An Analysis of Simplicity and Efficiency in Cooking

by Nomin Batjargal and An-Chi Lu

An exploratory data analysis investigating the relationship between recipe simplicity, step counts, preparation time, and user ratings. 

**[View the Live Interactive Report](https://nomin709.github.io/analysis_for_recipes/)**

---

## Overview

As life gets busy, home cooks and students alike often prioritize speed and minimal preparation over elaborate kitchen techniques. This project investigates whether fewer recipe steps correlate with higher ratings, lower prep times, or specific culinary categories.

### Data

The dataset used can be found [here](https://drive.google.com/drive/u/0/folders/1Tj34RInQA0rmarLuQO9hr-yqGhj-nkGX). It was originally scraped and used by the authors of [this](https://cseweb.ucsd.edu/~jmcauley/pdfs/emnlp19c.pdf) recommender systems paper. However, this provided dataset contains a subset of the raw data used in the original report, containing only the recipes and reviews posted since 2008. The full scraped raw data can be found [here](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions/data) on Kaggle.

### Key Highlights
- **Exploratory Data Analysis:** Univariate and bivariate distributions of cooking steps, preparation minutes, and user scores.
- **Missingness & Bias:** Statistical assessment of missing ratings and mechanism evaluations (MCAR, MAR, NMAR).
- **Hypothesis Testing & Prediction:** Framing predictive questions around recipe complexity and satisfaction metrics.
- **Interactive Report:** Built with Jekyll (customized Slate theme) featuring dynamic table-of-contents tracking and responsive data tables.

---

## Project Environment & Setup

This repository uses **Bundler (`Gemfile`)** to manage local Jekyll static site builds and **Docker** for a reproducible runtime environment across different operating systems.

### 1. The `Gemfile`
The `Gemfile` manages the Ruby dependencies required to compile the static site locally.

* **Purpose:** Ensures the local Jekyll version, Sass compiler, and plugins match the exact environment GitHub Pages uses to build the site in production (via the `github-pages` gem suite).
* **Usage:**
  ```bash
  # Install locked Ruby gems
  bundle install

  # Run the local Jekyll development server
  bundle exec jekyll serve

### 2. `docker-compose.yml`
`docker-compose.yml` defines and configures the container service needed to run the Jekyll environment with a single command.

* **Purpose:** Simplifies container management by automatically mapping ports, setting up environment variables, and mounting local files without needing to run long, manual Docker commands.
* **Usage:**
  ```bash
  # Start the local development server (live reloads on file changes)
  docker compose up

  # Stop and remove the running container
  docker compose down
