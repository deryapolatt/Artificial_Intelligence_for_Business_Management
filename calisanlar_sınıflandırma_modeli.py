import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("e__train.csv")
df.drop(['BusinessTravel', 'DistanceFromHome', 'Education', 'EmployeeCount', 'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsWithCurrManager'], axis=1, inplace=True)

one_hot_encoded = pd.get_dummies(df['Department'])
one_hot_encoded
df = pd.concat([df, one_hot_encoded], axis=1)
one_hot_encoded = pd.get_dummies(df['EducationField'])
one_hot_encoded
df = pd.concat([df, one_hot_encoded], axis=1)

X = df.drop(['Attrition', 'Department', 'EducationField'], axis=1).values
y = df["Attrition"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Support Vector Machine": SVC(),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    scores[model_name] = score

scores_df = pd.DataFrame(scores.items(), columns=["Model", "Score"])
#skor: accuracy değerleri

#Model Verimliliği Arttırma

#Random Forest Modeli

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df.drop(['Attrition', 'Department', 'EducationField'], axis=1).values
y = df["Attrition"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

random_forest = RandomForestClassifier(max_depth=5, min_samples_split=5, n_estimators=100)

random_forest.fit(X_train, y_train)

y_pred = random_forest.predict(X_test)

accuracy = random_forest.score(X_test, y_test)
print("Model Accuracy:", accuracy)


from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10]
}

rf_model = RandomForestClassifier()
grid_search = GridSearchCV(rf_model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

best_rf_model = grid_search.best_estimator_
best_rf_model.fit(X_train, y_train)

score = best_rf_model.score(X_test, y_test)
print("Random Forest - En iyi parametreler:", grid_search.best_params_)
print("Random Forest - Doğruluk skoru:", score)