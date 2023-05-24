import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix, classification_report, log_loss

df = pd.read_csv("Iris.csv")

# print(df)

# print(df.describe())

# print(df.shape)

# print(df.isna())

# print(df.columns)

# print(df.isna().sum())

# sns.heatmap(df.corr(), annot=True, cmap="Greens")
# plt.show()

def Remove_outlier(df,var):
	final_df = []
	q1 = df[var].quantile(0.25)
	q3 = df[var].quantile(0.75)
	iqr = q3-q1
	mini=q1-1.5*iqr
	maxi=q3+1.5*iqr
	for j in df[var]:
		if(j<mini or j>maxi):
			final_df.append(j)
			df.drop(df.loc[df[var]==j].index, inplace=True)


Remove_outlier(df,"SepalLengthCm")
Remove_outlier(df,"SepalWidthCm")
Remove_outlier(df,"PetalLengthCm")
Remove_outlier(df,"PetalWidthCm")

x = df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y = df["Species"]

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = GaussianNB()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

# print(y_pred)

print("Score Of the model before Normalization : ",model.score(x_test,y_test)) #0.65


clf_report = classification_report(y_test,y_pred)
print(clf_report)


features = np.array([[1,1,1,1]])
predictions = model.predict(features)
print("Predictions : {}".format(predictions))



