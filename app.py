import streamlit as st
import pandas as pd
import joblib

# Load files
model = joblib.load('KNN_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title('CardioPredict❤️')
st.markdown("Provide the following details")

# Inputs
age = st.slider('Age', 18, 100, 40)
sex = st.selectbox('Sex', ['Male', 'Female'])
chest_pain = st.selectbox('Chest Pain Type', ["ATA", 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 80, 200, 120)
cholesterol = st.number_input('Cholesterol (mg/dl)', 100, 600, 200)
fasting_bs = st.selectbox('Fasting Blood Sugar >120 mg/dl', [0, 1])
resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
max_hr = st.slider('Max Heart Rate', 60, 220, 150)
exercise_angina = st.selectbox('Exercise Induced Angina', ['Y', 'N'])
oldpeak = st.slider('Oldpeak', 0.0, 6.0, 1.0)
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

if st.button('Predict'):

    # Create raw input
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,

        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Add missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Keep only training columns order
    input_df = input_df[expected_columns]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)[0]

    # Probability (safe)
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(scaled_input)[0][1]
    else:
        probability = 0.0

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

