import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("student_data2.csv")
df.to_excel("student_data2.xlsx",index=False)
df.head()

df.tail()

df.shape

df.columns

df.duplicated().sum()

df.describe()

print(df['Marks'].mean())
print(df['Marks'].median())
print(df['Marks'].mode())

plt.hist(df['Marks'],bins=10)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()

plt.boxplot(df['Marks'])
plt.xlabel("Marks")
plt.title("Marks Distribution")
plt.show()

corr=df.corr(numeric_only=True)
print(corr)

print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
