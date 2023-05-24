import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv("Iris.csv")
print(df.describe())

sns.histplot(data=df,x='SepalLengthCm')
plt.show()

sns.histplot(data=df,x='SepalLengthCm',hue='Species',multiple='dodge')
plt.show()

sns.boxplot(data=df,x='SepalLengthCm')
plt.show()

sns.boxplot(data=df,x='SepalLengthCm', y='Species',hue='Species')
plt.show()