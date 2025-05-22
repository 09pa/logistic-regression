from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model
model = joblib.load("titanic_model.pkl")

# Create FastAPI app
app = FastAPI()

# Define input structure using Pydantic
class Passenger(BaseModel):
    pclass: int
    sex: int         # 0 = female, 1 = male
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: int    # 0 = C, 1 = Q, 2 = S (assumed label-encoded)

# API route to predict survival
@app.post("/predict")
def predict_survival(data: Passenger):
    # Convert input to DataFrame with correct column names
    input_df = pd.DataFrame([[
        data.pclass,
        data.sex,
        data.age,
        data.sibsp,
        data.parch,
        data.fare,
        data.embarked
    ]], columns=['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked'])

    # Predict
    prediction = model.predict(input_df)
    result = "Survived" if prediction[0] == 1 else "Did not survive"
    return {"prediction": result}
#to use this please uvicorn app:main --reload   <<<<---- run command in terminal