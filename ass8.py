#import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read Dataset
df=pd.read_csv('titanic.csv')
print("Titanic dataset is successfully loaded into Data Frame....")


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

#Fill the missing values
df ["Age"].fillna (df["Age"].median(), inplace=True)
print ("Null values are: \n",df.isnull().sum())


sns.histplot(data=df,x='Age')
plt.show()
sns.histplot(data=df,x='Fare')
plt.show()
sns.histplot(data=df,x='Age',hue='Sex',multiple='dodge',shrink=.8)
plt.show()
sns.histplot(data=df,x='Fare',hue='Sex',multiple='dodge',shrink=.8)
plt.show()

sns.distplot(df['Age'],kde=False)
plt.show()