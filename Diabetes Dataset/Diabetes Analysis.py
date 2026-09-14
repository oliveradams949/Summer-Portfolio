import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"c:\Users\Ollie\Uni Stuff\Summer Coding\Datasets\Diabetes Dataset\diabetes_data.zip")

print("--- Dataset Information ---")
print(df.info())


print("--- Dataset Shape ---")
print(df.shape)


print("--- Dataset Head ---")
print(df.head())



positive_diabetes = df[df["Outcome"] == 1]

negative_diabetes = df[df["Outcome"] == 0]

print(positive_diabetes.head())

average_glucose=df["Glucose"].mean()

exceed_glucose=df[df["Glucose"]>average_glucose]

diabetes_number_exceed  = exceed_glucose["Outcome"].value_counts()

melted_exceed = pd.melt(
    frame=exceed_glucose,
    id_vars=["Pregnancies", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"],
    value_vars=["Outcome"],
    var_name="Demographic",
    value_name="Status"
)

sorted_melted_exceed= melted_exceed.sort_values(by="Age", ascending=True)

"""
These 2 graphs show a very large number of values at 0 for skin thickness and insulin. This shows that a large number of values are left as zero when they likely shouldn't, showing that there isn't just a large cohort of those with
insulin levels of 0. Many have skin thickness of 0s and insulins of 0, so this likely isn't just type 1 diabetes and is instead blank values. I could also remove only those that are non-diabetic, however, according to the
Wikipedia for the population the study was conducted on, the study is largely type 2 diabetes, so would the trial would screen out those with biologically 0 insulin. So we can see it as blank values.

The last graph shows those with missing skin thickness and there skin thickness plotted against insulin. This leads to a graph that has a single lone point at 0, which shows that whenever there was skin thickness at 0, insulin was also at 0.
We also know by the last lines in the section that there are 227 patients with 0 as their skin thickness, and that all of those have 0 insulin. Therefore, the missingness is almost entirely uniform, although 392 patients have missing values. 
"""

sns.lmplot(data=df, x="SkinThickness", y="Glucose", col="Outcome", scatter_kws={'alpha':0.2, "s":10}, line_kws={"linewidth":3, "color":"black"})

plt.figure()

sns.scatterplot(data=df, x="SkinThickness", y="Insulin", hue="Outcome", alpha=0.7)

plt.figure()

skin_null = df[df["SkinThickness"]==0]

sns.scatterplot(data=skin_null, x="SkinThickness", y="Insulin", hue="Outcome", alpha=0.7)

plt.show()

print(skin_null.value_counts())

print(skin_null[skin_null["Insulin"]==0].value_counts())

"""
This looks through the columns we want no 0s in, and then replaces with a null value. Then, it prints the count of those rows that have null values in each column. 
"""

replace_value = ["Age", "SkinThickness", "Insulin", "BMI", "BloodPressure", "Glucose", "DiabetesPedigreeFunction"]

df[replace_value] = df[replace_value].replace(0,np.nan)

print(df.isnull().sum())

"""
In order to train a model on the data, the null values must be replaced with a suitable placeholder. This allows the model to be trained appropriately. From what I can tell online, using imputation to replace the nulls with the median
seems to be the best approach. However, which must investigate the distribution of the null values first, splitting the dataset into a healthy cohort and then summing the nulls again. We then find the proportions of nulls, and compare
with the initial dataset. This is largely to test the hypothesis as to whether those taking the measurements were doing so as the patient tested positive or negative, and so the measurements weren't taken due to that. Similar to the 
reasoning laid out in one of the previous summaries.
"""
print((df.isnull().sum()/len(df)*100).round(1))

healthy_df = df[df["Outcome"] == 0]

print(((healthy_df[replace_value].isnull().sum()/ len(healthy_df))*100).round(1))
"""
This shows the distribution of the nulls, with the values being incredibly close together for both the initial and healthy dataset (48.7% vs 47.2% for Insulin). This suggests that whether or not the patient had tested positive had no bearing on the presence of null
values. This shows how using a global median would lead to an incredible large flattening of the data, as the nulls are evenly spread. Due to the nature of glucose levels within diabetics, this would lead to a flattening of outliers and
so a major decrease in the R^2 and increase in the MAE of any potential model, reducing it's predictive power and reliability. As such, a more advanced approach would be appropriate.
"""