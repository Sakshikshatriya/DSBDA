import pandas as pd

df=pd.read_csv('Employee_Salary.csv')

print(df)

print(df.describe())

# print("Mean of Years of Experience : ",df["YearsExperience"].mean())
# print("Median of Years of Experience : ",df["YearsExperience"].median())
# print("Standard Deviation of Years of Experience : ",df["YearsExperience"].std())
# print("Minimum of Years of Experience : ",df["YearsExperience"].min())
# print("Maximum of Years of Experience : ",df["YearsExperience"].max())
# print("Standard Deviation of Years of Experience : ",df["YearsExperience"].std())

print("Mean of Salary : ",df["Salary"].mean())
print("Median of Salary : ",df["Salary"].median())
print("Standard Deviation of Salary : ",df["Salary"].std())
print("Minimum of Salary : ",df["Salary"].min())
print("Maximum of Salary : ",df["Salary"].max())
print("Standard Deviation of Salary : ",df["Salary"].std())

print("Mean of Age : ",df["Age"].mean())
print("Median of Age : ",df["Age"].median())
print("Standard Deviation of Age : ",df["Age"].std())
print("Minimum of AgeAgeAgeAge : ",df["Age"].min())
print("Maximum of Age : ",df["Age"].max())
print("Standard Deviation of Age : ",df["Age"].std())

# print("\t","\t","YearsExperience","\t","Salary","\t\t","Age")
# print("Mean","\t\t",df["YearsExperience"].mean(),"\t",df["Salary"].mean(),"\t\t",df["Age"].mean())
# print("Median","\t\t",df["YearsExperience"].median(),"\t\t\t",df["Salary"].median(),"\t\t",df["Age"].median())
# print("Mode","\t\t",df["YearsExperience"].mode(),"\t",df["Salary"].mode(),"\t",df["Age"].mode())
# print("Std","\t\t",df["YearsExperience"].std(),"\t",df["Salary"].std(),"\t",df["Age"].std())
# print("Min","\t\t",df["YearsExperience"].min(),"\t\t\t",df["Salary"].min(),"\t\t\t",df["Age"].min())
# print("Max","\t\t",df["YearsExperience"].max(),"\t\t\t",df["Salary"].max(),"\t\t",df["Age"].max())
print()

print(df["Salary"].groupby(df["Age"]).count())
print()

print("Mean : ",df["Salary"].groupby(df["Age"]).mean())
print("Median : ",df["Salary"].groupby(df["Age"]).median()) 
print("Std : ",df["Salary"].groupby(df["Age"]).std())


print(df.groupby(df["Age"]).describe().transpose)

print("\tyears of experience\tsalary\t\tage")
print("count","\t",df["Experience_Years"].count(),"\t\t\t",df["Salary"].count())
print("mean\t",df["Experience_Years"].mean(),"\t\t",df["Salary"].mean())
print("median\t{:.6f}\t\t{:.6f}\t{:.6f}".format(df["Experience_Years"].median(),df["Salary"].median(),df["Age"].median()))
print("std\t{:.6f}\t\t{:.6f}".format(df["Experience_Years"].std(),df["Salary"].std()))

print("salary group by age ",(df["Salary"].groupby(df["Age"]).count()))