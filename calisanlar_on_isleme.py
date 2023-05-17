import pandas as pd
df = pd.read_csv("e__train.csv")
df.drop(['BusinessTravel', 'DistanceFromHome', 'Education', 'EmployeeCount', 'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsWithCurrManager'], axis=1, inplace=True)

one_hot_encoded = pd.get_dummies(df['Department'])
one_hot_encoded
df = pd.concat([df, one_hot_encoded], axis=1)
one_hot_encoded = pd.get_dummies(df['EducationField'])
one_hot_encoded
df = pd.concat([df, one_hot_encoded], axis=1)

df
