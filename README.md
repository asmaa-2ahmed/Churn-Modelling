# Churn Modelling Dataset

## Overview

The Churn Modelling dataset is designed to assist data scientists and analysts in developing models to predict customer churn in the banking sector. Customer churn refers to the phenomenon where customers discontinue their relationship with a company. By analyzing this dataset, one can identify patterns and factors contributing to customer attrition, enabling businesses to implement strategies to retain customers.

## Dataset Source

The dataset is available on Kaggle: [Churn Modelling Dataset](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)

## Dataset Structure

The dataset comprises 10,000 rows, each representing a unique customer, and 14 columns with the following attributes:

| Column Name       | Data Type         | Description                                                                 |
|-------------------|-------------------|-----------------------------------------------------------------------------|
| RowNumber         | Integer           | Index of the row.                                                           |
| CustomerId        | Integer           | Unique identifier for each customer.                                        |
| Surname           | String            | Customer's surname.                                                         |
| CreditScore       | Integer           | Credit score of the customer.                                               |
| Geography         | String            | Country of residence (e.g., France, Spain, Germany).                        |
| Gender            | String            | Gender of the customer (Male or Female).                                    |
| Age               | Integer           | Age of the customer.                                                        |
| Tenure            | Integer           | Number of years the customer has been with the bank.                        |
| Balance           | Float             | Account balance of the customer.                                            |
| NumOfProducts     | Integer           | Number of products the customer has with the bank.                          |
| HasCrCard         | Integer (0 or 1)  | Indicates if the customer has a credit card (1 = Yes, 0 = No).              |
| IsActiveMember    | Integer (0 or 1)  | Indicates if the customer is an active member (1 = Yes, 0 = No).            |
| EstimatedSalary   | Float             | Estimated annual salary of the customer.                                    |
| Exited            | Integer (0 or 1)  | Indicates if the customer has churned (1 = Yes, 0 = No).                    |

## Usage

This dataset is suitable for:

- **Exploratory Data Analysis (EDA):** Understanding the distribution and relationships of customer attributes.
- **Feature Engineering:** Creating new features to improve model performance.
- **Model Training:** Building classification models to predict customer churn.
- **Model Evaluation:** Assessing model performance using metrics like accuracy, precision, recall, and F1-score.

## Getting Started

To begin using the dataset:

1. **Download:** Access and download the dataset from [Kaggle](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling).
2. **Load:** Use data analysis libraries such as Pandas in Python to load the dataset.
3. **Analyze:** Perform exploratory data analysis to understand the data.
4. **Preprocess:** Handle missing values, encode categorical variables, and scale numerical features as needed.
5. **Model:** Apply machine learning algorithms to predict the 'Exited' status.

## Acknowledgements

The dataset is provided by [Kaggle](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling) for educational and research purposes. 