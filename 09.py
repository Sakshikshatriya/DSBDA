import pandas as pd
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv("titanic.csv")
print(df.columns)
sns.boxplot(data=df,x='Age',y='Sex',hue='Survived')
plt.show()