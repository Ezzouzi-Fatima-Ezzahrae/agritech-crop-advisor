import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


# -------------------------------
# STEP 1: Create dataset (same as before)
# -------------------------------
data = {
    'N': [90, 85, 60, 74, 78, 69, 69, 94, 89, 68],
    'P': [42, 58, 55, 35, 42, 37, 55, 53, 54, 58],
    'K': [43, 41, 44, 40, 42, 38, 44, 40, 38, 40],
    'temperature': [20.8, 22.2, 23.0, 26.5, 24.0, 23.5, 25.0, 21.0, 22.5, 24.5],
    'humidity': [82, 80, 78, 75, 77, 76, 74, 83, 81, 79],
    'ph': [6.5, 6.4, 6.3, 6.7, 6.6, 6.5, 6.4, 6.8, 6.7, 6.6],
    'rainfall': [200, 180, 150, 120, 130, 140, 110, 210, 190, 160],
    'label': ['rice', 'rice', 'maize', 'maize', 'maize',
              'wheat', 'wheat', 'rice', 'rice', 'maize']
}

dataset = pd.DataFrame(data)

# -------------------------------
# STEP 2: Train model
# -------------------------------
X = dataset.drop(columns=['label'])
y = dataset['label']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# -------------------------------
# STEP 3: Streamlit UI
# -------------------------------
st.title("🌱 Crop Recommendation System")

st.write("Enter soil and weather conditions:")

N = st.number_input("Nitrogen (N)", 0, 150, 90)
P = st.number_input("Phosphorus (P)", 0, 100, 40)
K = st.number_input("Potassium (K)", 0, 100, 40)
temperature = st.number_input("Temperature", 0.0, 50.0, 25.0)
humidity = st.number_input("Humidity", 0.0, 100.0, 80.0)
ph = st.number_input("pH", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall", 0.0, 300.0, 150.0)

# -------------------------------
# STEP 4: Prediction
# -------------------------------
if st.button("Predict Crop"):
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(input_data)

    st.success(f"🌾 Recommended Crop: {prediction[0]}")
joblib.dump(model, "model.pkl")    