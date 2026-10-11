import pandas as pd
import joblib

model = joblib.load("ml/placement_model.pkl")

student = pd.DataFrame({
    "attendance": [85],
    "cgpa": [8.2]
})

prediction = model.predict(student)

if prediction[0] == 1:
    print("Student will be placed")
else:
    print("Student may not be placed")
