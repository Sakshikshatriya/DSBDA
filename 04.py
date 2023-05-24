import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np 

df = pd.read_csv("HousingData.csv")

print(df.info)
print(df.shape)
print(df.size)
print(df.columns)
print(df.dtypes)
print(df.head())
print(df.tail())
print(df.sample(4))
print(df.isna().sum())

#remove null values

df['CRIM']=df['CRIM'].fillna(df['CRIM'].mean())
df['ZN']=df['ZN'].fillna(df['ZN'].mean())
df['CHAS']=df['CHAS'].fillna(df['CHAS'].mean())
df['AGE']=df['AGE'].fillna(df['AGE'].mean())
df['LSTAT']=df['LSTAT'].fillna(df['LSTAT'].mean())
df['INDUS']=df['INDUS'].fillna(df['INDUS'].mean())

print(df.isna().sum())


#HEATMAP

sns.heatmap(df.corr(),annot=True)
plt.show()

#DISPLAY OUTLIERS

sns.boxplot(data=df,x='RM')
plt.show()
sns.boxplot(df['LSTAT'])
plt.show()
sns.boxplot(df['MEDV'])
plt.show() 

# REMOVE OUTLIERS

def remove_outliers(df,var):

    q1=df[var].quantile(0.25)
    q3=df[var].quantile(0.75)
    IQR = q3-q1
    min = q1-1.5*IQR
    max = q3+1.5*IQR
    for i in df[var]:
        if i<=min or i>=max:
            df.drop(df.loc[df[var]==i].index, inplace=True)

    
remove_outliers(df,'RM')
remove_outliers(df,'MEDV')
remove_outliers(df,'LSTAT')

sns.boxplot(data=df,x='RM')
plt.show()
sns.boxplot(df['LSTAT'])
plt.show()        
sns.boxplot(df['MEDV'])
plt.show() 


x=df[['RM','LSTAT']]
y=df['MEDV']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression

model= LinearRegression().fit(x_train,y_train)
y_predict=model.predict(x_test)
print(y_predict)

#display accuracy of model
from sklearn.metrics import mean_absolute_error
print("MAE:",mean_absolute_error(y_test,y_predict))
print("model score:",model.score(x_test,y_test))

features= np.array([[6,17]])
prediction=model.predict(features)
print(prediction)