# CardioPredict❤️ 

A Machine Learning web application that predicts the risk of heart disease using a K-Nearest Neighbors (KNN) classifier. The model is trained on medical attributes and deployed with an interactive Streamlit frontend.

---

## 🚀 Features

* Predicts heart disease risk (Low / High)
* Uses KNN Classifier
* Interactive Streamlit UI
* Pre-trained model loaded using `.pkl` file
* Real-time predictions
* Clean and simple interface

---

## 🧠 Machine Learning Details

* Algorithm: K-Nearest Neighbors (KNN)
* Model file: `model.pkl`
* column file: `columns.pkl`
* Scaler used for preprocessing
* Binary classification output

---

## 📂 Project Structure

```
├── app.py
├── model.pkl
├── scaler.pkl (if applicable)
├── columns.pkl 
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/mukul1421/CardioPredict-ML

Navigate to project folder:

cd your-repo-name

Create virtual environment:

python -m venv env

Activate environment:

**Windows**

env\Scripts\activate

**Mac/Linux**

source env/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## ▶️ Run the App

streamlit run app.py

---

## 📊 Input Features

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Max Heart Rate
* Exercise Angina
* Oldpeak
* ST Slope

---

## 📌 Output

* Low Risk of Heart Disease
* High Risk of Heart Disease

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Streamlit
* Pandas
* NumPy
* Pickle

---

## 👨‍💻 Author

Mukul

---

## ⭐ If you like this project or it helps you 

Give it a star on GitHub!
