import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
df=pd.read_csv("students.csv")
X=df[["attendance","cgpa"]]
y=df["placed"]
model=DecisionTreeClassifier()
model.fit(X,y)
joblib.dump(model,"placement_model.pkl")
print("model saved")
