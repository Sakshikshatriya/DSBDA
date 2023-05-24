import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Social_Network_Ads.csv')

print(df.info)
print(df.columns)
print(df.shape)

print(df.isna().sum())

# sns.heatmap(df.corr(),annot=True)
# plt.show()

sns.boxplot(data=df,x='Age')
plt.show()

sns.boxplot(data=df,x='EstimatedSalary')
plt.show()
x=df[['Age','EstimatedSalary']]
y=df['Purchased']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler
x_train=StandardScaler().fit_transform(x_train)
x_test=StandardScaler().fit_transform(x_test)


from sklearn.linear_model import LogisticRegression
model=LogisticRegression().fit(x_train,y_train)
y_predict=model.predict(x_test)
print(y_predict)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_predict))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_predict))
sns.heatmap(confusion_matrix(y_test,y_predict),annot=True)
plt.show()

# from sklearn.metrics import precision_recall_fscore_support, confusion_matrix, classification_report, log_loss

# score = precision_recall_fscore_support(y_test,y_predict, average="micro")
# print(score[3])




