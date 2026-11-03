
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [24, 27, 22, 32, 29, 25, 30, 100, 28, 35],
    'Salary': [50000, 60000, 52000, 58000, 62000,
               55000, 60000, 600000, 65000, 70000],
    'Tenure': [1, 2, 3, 4, 5, 6, 7, 8, None, 10],
    'Churn': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print("1. First Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nColumn Names:")
print(df.columns)


print("\n2. Descriptive Statistics:")
print(df.describe())

print("\nMean:")
print(df['Age'].mean())

print("\nMedian:")
print(df['Age'].median())

print("\nMode:")
print(df['Age'].mode()[0])

print("\nStandard Deviation:")
print(df['Age'].std())

print("\nVariance:")
print(df['Age'].var())

print("\nMinimum:")
print(df['Age'].min())

print("\nMaximum:")
print(df['Age'].max())

print("\nQuantiles:")
print(df['Age'].quantile([0.25, 0.5, 0.75]))



# Histogram
plt.hist(df['Age'].dropna(), bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

sns.boxplot(y=df['Age'])
plt.title('Box Plot of Age')
plt.show()

plt.scatter(df['Age'], df['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

corr_matrix = df.select_dtypes(include='number').corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


print("\n4. Missing Values:")
print(df.isnull())

print("\nNumber of Missing Values:")
print(df.isnull().sum())

print("\nAfter Dropping Missing Values:")
print(df.dropna())

df_filled = df.copy()
df_filled = df_filled.fillna(df_filled.mean(numeric_only=True))

print("\nAfter Filling Missing Values:")
print(df_filled)


df_outlier = df_filled.copy()

df_outlier['Age_zscore'] = zscore(df_outlier['Age'])
df_outlier['Salary_zscore'] = zscore(df_outlier['Salary'])

print("\n5. Z-Scores:")
print(df_outlier)

print("\nDetected Outliers:")
print(df_outlier[
    (df_outlier['Age_zscore'].abs() > 3) |
    (df_outlier['Salary_zscore'].abs() > 3)
])


df_no_outliers = df_outlier[
    (df_outlier['Age_zscore'].abs() <= 3) &
    (df_outlier['Salary_zscore'].abs() <= 3)
]

print("\n6. Dataset After Removing Outliers:")
print(df_no_outliers)


def cap_values(series):
    upper_limit = series.mean() + 3 * series.std()
    lower_limit = series.mean() - 3 * series.std()
    return series.clip(lower=lower_limit, upper=upper_limit)


df_outlier['Age_capped'] = cap_values(df_outlier['Age'])
df_outlier['Salary_capped'] = cap_values(df_outlier['Salary'])

print("\n7. Dataset After Capping Outliers:")
print(df_outlier[
    ['Age', 'Age_capped', 'Salary', 'Salary_capped']
])


print("\n8. Remaining Missing Values:")
print(df_filled.isnull().sum())

print("\nRemaining Outliers:")
print(df_no_outliers)

print("\nFinal Cleaned Dataset:")
print(df_no_outliers)



df_no_outliers.to_csv('cleaned_customer_churn.csv', index=False)

print("\n9. Cleaned Dataset Saved Successfully!")
