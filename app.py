import streamlit as st
import pandas as pd
import pickle 

# Load the trained model
scaler = pickle.load(open('scaler (1).pkl', 'rb'))
model = pickle.load(open('model_gbc (1).pkl', 'rb'))

df_dict = {
    'age': [age],
    'bp': [blood_pressure],
    'sg': [sg],
    'al': [al],
    'hemo': [hemoglobin],
    'sc': [sc],
    'htn': [htn],
    'dm': [dm],
    'cad': [cad],
    'appet': [appetite],
    'pc': [pe]
}
df = pd.DataFrame(df_dict) 

# Set up the Streamlit app
st.title("Chronic Kidney Disease Prediction App")
col1, col2 = st.columns(2)


with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=80.0)
    sg = st.number_input("Specific Gravity", min_value=1.0, max_value=1.05, value=1.02)
    al = st.number_input("Albumin", min_value=0.0, max_value=5.0, value=0.0)    
    hemoglobin = st.number_input("Hemoglobin", min_value=0.0, max_value=20.0, value=15.0)
    sc = st.number_input("Serum Creatinine", min_value=0.0, max_value=20.0, value=1.0)

with col2:
    htn = st.selectbox("Hypertension", ['No', 'Yes'])
    dm = st.selectbox("Diabetes Mellitus", ['No', 'Yes'])
    cad = st.selectbox("Coronary Artery Disease", ['No', 'Yes'])
    pe = st.selectbox("Proteinuria", ['No', 'Yes'])
    appetite = st.selectbox("Appetite", ['Good', 'Poor'])                     


if st.button("Predict"):
    result = predict_kidney_disease(age,blood_pressure,sg,al,hemoglobin,sc,htn,dm,cad,pe,appetite)    

if result == 1:
    st.error("The patient is likely to have chronic kidney disease.")
else:
    st.success("The patient is unlikely to have chronic kidney disease.")
