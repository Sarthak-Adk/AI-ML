Book Rating Predictor

A beginner machine learning project where I built a complete ML pipeline from scratch by scraping data, cleaning it, training models, and deploying it with Flask.

Project Overview

This project predicts book ratings (1–5 stars) using scraped data from Books to Scrape.

The goal of this project was to practice:

Web scraping
Data cleaning
Feature engineering
Model training
Model deployment

This is my first self-built end-to-end ML project.

Dataset Collection

I scraped 1000 books manually from the website.

Collected features:

Book Name
Price
Rating
Stock Availability
Category

The scraping process involved:

Pagination scraping
Nested scraping (visiting each book detail page)
Extracting category using breadcrumbs
Data Cleaning

Performed:

Removed unnecessary index column
Converted price from string to float
Extracted stock numbers from text
Encoded category labels into numeric values

Example:

Price:

£51.77 → 51.77

Stock:

In stock (22 available) → 22

Category:

Travel → 7
Machine Learning Pipeline

Pipeline:

Scrape → Clean → Encode → Train-Test Split → Train → Evaluate → Save Model

Features used:

price
stock
category

Target:

rating

Train-test split:

80% training
20% testing
Models Used
1. Logistic Regression

Used as baseline model.

Accuracy:

21%
2. Random Forest Classifier

Used for better non-linear learning.

Accuracy:

21%
Project Result (Failure Analysis)

This project failed to achieve high accuracy.

Reason:

The selected features were weak for predicting ratings.

Book ratings depend on hidden factors like:

writing quality
author popularity
content quality
reader preference

These features were not present in the dataset.

Main lesson learned:

Feature quality matters more than model complexity.

Even changing models did not improve performance.

This failure helped me understand real-world ML better.

Deployment

Built a Flask web app for prediction.

User inputs:

price
stock
category

Flask:

loads model
loads encoder
predicts rating

Files saved:

book_rating_model.pkl
category_encoder.pkl
Tech Stack
Python
pandas
Beautiful Soup
scikit-learn
Flask
joblib
What I Learned
Web scraping fundamentals
Nested scraping logic
Data cleaning techniques
Label encoding
Train-test split
Model evaluation
Saving models and encoders
Deploying ML models with Flask
Importance of feature engineering
Future Improvements

Possible improvements:

Add book descriptions
Add title length feature
Add author data
Add review counts
Use NLP on descriptions
Try advanced models
Author

Sarthak Adhikari

Beginner in Machine Learning, learning by building real projects.