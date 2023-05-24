import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# #Read Dataset
df=pd.read_csv("Student_data.csv")

#Display information of dataset
print(df.info)
print(df.shape)
print(df.columns)
print(df.head())
print(df.sample())
print(df.tail())
print(df.dtypes)

#Display statistical information of dataset
print(df.describe())

#Display null values
print(df.isna().sum())
print(df.isna())

#data type conversion
print("Converting Data type of variables: ")
df["sl_no"]=df[ "sl_no"].astype( "int8")
print("Check Datatype of sl_no",df.dtypes)
df[ "ssc_p"]=df[ "ssc_p"].astype("int8")
print("Check Datatype of ssc_p",df.dtypes)

# Label Encoding Conversion of Categorical to Quantitative
df['sex']=df["sex"].replace(['M','F'],[0,1],inplace=True)


# Normalization
print("Normalization using Min-Max Feature Scaling: ")
df["salary"]=(df["salary"]-df["salary"].min())/(df ["salary"].max()-df["salary"].min())
print(df.head().T)