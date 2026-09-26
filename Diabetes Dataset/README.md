# Diabetes Dataset (PIMA)

Exploratory Data-cleaning and analysis, conducted on a diabetes dataset. Largely used to discuss data imputation before models.

## Source Dataset
* **Dataset Link:** [Kaggle Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/mragpavank/diabetes)

## Description
* Analysed the distribution and the values inherent within the dataset.
* Showed how the dataset contains a large value of missing values, which are largely out of line with true biological measurements.
* Said missing values are not entirely distributed at random, as the missing values are intertwined (Skin thickness and insulin).
* Identified the proportion of missing values dependent upon the outcome (health of the patient) of the diabetes test conducted.
* Showed how the missingness is largely present in exceedingly similar proportions across negative vs positive outcomes.
* Used this pattern to evaluate whether a single-value imputation (e.g. median) is suitable, or whether the missingness present requires a more advanced approach.

## Future Improvements
* Utilise a more advanced imputation technique than a single value, such as KNN or MICE.
* Implement predictive models such as logistic regression in order to predict outcome. 
