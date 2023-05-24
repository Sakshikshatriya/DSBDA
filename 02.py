import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Student_performance.csv")

print(df.fillna(method='pad'))

#display outliers
sns.boxplot(data=df,x='raisedhands')
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

# Label Encoding Conversion of Categorical to Quantitative
df['sex']=df["sex"].replace(['M','F'],[0,1],inplace=True)

#show boxplot