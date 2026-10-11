from fastapi import FastAPI
from app.chatbot import ask_ai
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("ml/placement_model.pkl")

@app.get("/")
def home():
    return {"message": "AI Student Management"}

@app.get("/placement")
def placement(attendance: int, cgpa: float):
    data = pd.DataFrame({
        "attendance": [attendance],
        "cgpa": [cgpa]
    })

    prediction = model.predict(data)

    return {
        "prediction": int(prediction[0])
    }

@app.get("/chat")
def chat(question: str):

    answer = ask_ai(question)

    return {
        "question": question,
        "answer": answer
    }
