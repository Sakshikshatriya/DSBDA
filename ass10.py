import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read Dataset
df=pd.read_csv("iris.csv")
print("iris dataset is successfully loaded into Data Frame....")


#Display information of dataset
print( "Information of Dataset: \n", df.info)
print( "Shape of Dataset (row x column):",df.shape)
print( "Columns Name:", df.columns)
print( "Total elements in dataset:", df.size)
print( "Datatype of attributes (columns):", df.dtypes)
print( "First 5 rows: \n", df.head().T)
print( "Last 5 rows:\n",df.tail().T)
print( "Any 5 rows: \n",df.sample(5).T)

#Find missing values
print ("Missing values")
print(df.isnull().sum())

#Histogram of 1-variable
sns.histplot(data=df,x="SepalLengthCm")
sns.histplot(data=df,x="SepalWidthCm")
sns.histplot(data=df,x="PetalLengthCm")
sns.histplot(data=df,x="PetalWidthCm")
plt.show()

#Histogram of 2-variables
sns.histplot(data=df, x="SepalLengthCm",hue="variety", multiple="dodge")
sns.histplot(data=df, x="SepalWidthCm",hue="variety", multiple="dodge")
sns.histplot(data=df, x="PetalLengthCm",hue="variety", multiple ="dodge")
sns.histplot(data=df, x="PetalWidthCm",hue="variety", multiple="dodge")
plt.show()

#Boxplot of 1-variable.
sns.boxplot(data=df,x="SepalLengthCm")
sns.boxplot(data=df,x="SepalWidthCm")
sns.boxplot(data=df,x="PetalLengthCm")
sns.boxplot(data=df,x="PetalWidthCm")
plt.show()


#Boxplot of 2-variables
sns.boxplot(data=df, x="SepalLengthCm",y="variety", hue="variety")
sns.boxplot(data=df, x="SepalWidthCm",y="variety", hue="variety")
sns.boxplot(data=df, x="PetalLengthCm",y="variety", hue="variety")
sns.boxplot(data=df, x="PetalWidthCm",y="variety", hue="variety")
plt.show()