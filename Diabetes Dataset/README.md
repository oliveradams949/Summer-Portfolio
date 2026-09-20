# Diabetes Dataset (PIMA)

Exploratory Data-cleaning and analysis, conducted on a diabetes dataset. Largely used to discuss data imputation before models.

## Source Dataset
* **Dataset Link:** [Kaggle Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/mragpavank/diabetes)

## Description
* Analysed the distribution and the values inherent within the dataset.
* Shows how the dataset contains a large value of missing values.
* Said missing values are not entirely distributed at random, as the missing values are intertwined (Skin thickness and insulin).
* Identifies the proportion of missing values dependent upon the outcome (health of the patient) of the diabetes test conducted.
* Shows how the missingness is largely present in similar proportions across negative vs positive outcomes.
* Uses this pattern to evaluate whether a single-value imputation (e.g. median) is suitable, or whether the missingness present requires a more targeted approach.
## Future Improvements
* Utilise a more advanced imputation technique than a single value, such as KNN or MICE.
* Implement predictive models such as logistic regression in order to predict outcome. 
