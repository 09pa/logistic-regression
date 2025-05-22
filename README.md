# 🚢 Titanic Survival Prediction API (Logistic Regression + FastAPI)

This project uses a **Logistic Regression model** trained on the Titanic dataset and deployed using **FastAPI**. You can predict survival probability for individual or multiple passengers using a REST API.

---

## 📦 Features

- ✅ Logistic Regression with scikit-learn
- ✅ Cleaned Titanic dataset with 7 features
- ✅ `/predict` for single input
- ✅ `/batch_predict` for multiple passengers
- ✅ API powered by FastAPI
- ✅ Ready for local testing with Postman or cURL

---

## 🎯 Features Used for Prediction

- `age`: Passenger’s age *(float)*
- `pclass`: Ticket class *(1, 2, 3)*
- `sex`: `'male'` or `'female'`
- `sibsp`: # of siblings/spouses aboard *(int)*
- `parch`: # of parents/children aboard *(int)*
- `fare`: Ticket fare *(float)*
- `embarked`: Port of Embarkation *(‘C’, ‘Q’, ‘S’)*

---

## 🛠 How to Run

### 1. Clone this repo:
```bash
git clone https://github.com/your-username/logistic-regression.git
cd logistic-regression
```

### 2. Create and activate a virtual environment:
```bash
python -m venv venv
# Activate:
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3. Install required packages:
```bash
pip install -r requirements.txt
```

### 4. Launch the FastAPI server:
```bash
uvicorn app:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API via Swagger UI.

---

## 🔍 API Endpoints

### 🟢 `GET /`
Health check

```json
{
  "msg": "Titanic Survival Prediction API is live!"
}
```

---

### 🟡 `POST /predict`
Predict survival for **one passenger**

#### Request JSON:
```json
{
  "age": 28,
  "pclass": 2,
  "sex": "female",
  "sibsp": 0,
  "parch": 0,
  "fare": 25.5,
  "embarked": "S"
}
```

#### Response:
```json
{
  "prediction": 1
}
```
> `1` = Survived, `0` = Did not survive

---

### 🔵 `POST /batch_predict`
Predict survival for **multiple passengers**

#### Request JSON:
```json
{
  "passengers": [
    {
      "age": 28,
      "pclass": 2,
      "sex": "female",
      "sibsp": 0,
      "parch": 0,
      "fare": 25.5,
      "embarked": "S"
    },
    {
      "age": 40,
      "pclass": 3,
      "sex": "male",
      "sibsp": 1,
      "parch": 0,
      "fare": 15.0,
      "embarked": "Q"
    }
  ]
}
```

#### Response:
```json
{
  "predictions": [1, 0]
}
```

---

## 📬 How to Test in Postman

### Single Prediction:

- Method: `POST`
- URL: `http://127.0.0.1:8000/predict`
- Body → raw → JSON:
```json
{
  "age": 22,
  "pclass": 3,
  "sex": "male",
  "sibsp": 1,
  "parch": 0,
  "fare": 7.25,
  "embarked": "S"
}
```

---

### Batch Prediction:

- Method: `POST`
- URL: `http://127.0.0.1:8000/batch_predict`
- Body → raw → JSON:
```json
{
  "passengers": [
    {
      "age": 34,
      "pclass": 2,
      "sex": "male",
      "sibsp": 0,
      "parch": 0,
      "fare": 12.0,
      "embarked": "C"
    },
    {
      "age": 18,
      "pclass": 1,
      "sex": "female",
      "sibsp": 1,
      "parch": 1,
      "fare": 80.0,
      "embarked": "S"
    }
  ]
}
```

---

## 📂 Project Structure

```
├── app.py               # FastAPI app
├── titanic_model.pkl    # Trained model
├── notebook.ipynb       # EDA + training code
├── requirements.txt     # Dependencies
├── README.md            # This file
```

---

## 👨‍💻 Author

Parth Kahar  
GitHub: [09pa](https://github.com/09pa)

---

## 📜 License

MIT License
