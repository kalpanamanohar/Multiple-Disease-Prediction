import streamlit as st
import pickle
import numpy as np
import time

# Load models
kidney_model = pickle.load(open("best_model_kidney.pkl", "rb"))
liver_model = pickle.load(open("best_model_liver.pkl", "rb"))
parkinson_model = pickle.load(open("best_model_parkinson.pkl", "rb"))

st.set_page_config(page_title="Disease Prediction App", page_icon="🧬", layout="centered")
st.title("🧬 Multiple Disease Prediction App")
st.markdown("Predict **Kidney**, **Liver**, and **Parkinson’s Disease** with probability and risk level indicators.")

# Sidebar selection
disease = st.sidebar.selectbox("Select Disease:", ["Kidney Disease", "Liver Disease", "Parkinson’s Disease"])

# Risk level categorization
def risk_level(prob):
    if prob < 0.3:
        return "🟢 Low Risk"
    elif prob < 0.7:
        return "🟠 Moderate Risk"
    else:
        return "🔴 High Risk"

# Unified result display
def show_result(pred, prob, name):
    st.subheader("🩺 Prediction Result")
    risk = risk_level(prob)
    
    if pred == 1:
        st.error(f"⚠️ The patient **is likely to have {name}**.")
    else:
        st.success(f"✅ The patient is **not likely to have {name}**.")
    
    st.markdown("### 📊 Disease Probability & Risk")
    progress_value = int(prob * 100)
    progress = st.progress(0)
    for i in range(progress_value + 1):
        time.sleep(0.01)
        progress.progress(i)
    
    st.metric(label=f"Predicted Probability for {name}", value=f"{prob*100:.2f}%")
    st.info(f"Risk Level: {risk}")

# ---------------------- Kidney Disease ----------------------
if disease == "Kidney Disease":
    st.header("🩺 Kidney Disease Prediction")

    # Numeric fields
    age = st.number_input("Age", 0, 120, 45)
    bp = st.number_input("Blood Pressure", 0.0, 200.0, 80.0)
    sg = st.number_input("Specific Gravity", 1.0, 1.05, 1.02)
    al = st.number_input("Albumin", 0.0, 5.0, 1.0)
    su = st.number_input("Sugar", 0.0, 5.0, 0.0)
    bgr = st.number_input("Blood Glucose Random", 0.0, 500.0, 120.0)
    bu = st.number_input("Blood Urea", 0.0, 300.0, 50.0)
    sc = st.number_input("Serum Creatinine", 0.0, 15.0, 1.2)
    sod = st.number_input("Sodium", 100.0, 200.0, 135.0)
    pot = st.number_input("Potassium", 0.0, 10.0, 4.5)
    hemo = st.number_input("Hemoglobin", 3.0, 20.0, 13.5)
    pcv = st.number_input("Packed Cell Volume", 0.0, 60.0, 40.0)
    wc = st.number_input("White Blood Cell Count", 0.0, 25000.0, 8000.0)
    rc = st.number_input("Red Blood Cell Count", 0.0, 10.0, 4.8)

    # Categorical (encoded 0/1)
    rbc = 1 if st.selectbox("Red Blood Cells", ["Normal", "Abnormal"]) == "Normal" else 0
    pc = 1 if st.selectbox("Pus Cell", ["Normal", "Abnormal"]) == "Normal" else 0
    pcc = 1 if st.selectbox("Pus Cell Clumps", ["Not Present", "Present"]) == "Present" else 0
    ba = 1 if st.selectbox("Bacteria", ["Not Present", "Present"]) == "Present" else 0
    htn = 1 if st.selectbox("Hypertension", ["No", "Yes"]) == "Yes" else 0
    dm = 1 if st.selectbox("Diabetes Mellitus", ["No", "Yes"]) == "Yes" else 0
    cad = 1 if st.selectbox("Coronary Artery Disease", ["No", "Yes"]) == "Yes" else 0
    appet = 1 if st.selectbox("Appetite", ["Poor", "Good"]) == "Good" else 0
    pe = 1 if st.selectbox("Pedal Edema", ["No", "Yes"]) == "Yes" else 0
    ane = 1 if st.selectbox("Anemia", ["No", "Yes"]) == "Yes" else 0

    if st.button("Predict Kidney Disease"):
        features = np.array([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc,
                              sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])
        pred = kidney_model.predict(features)[0]
        prob = kidney_model.predict_proba(features)[0][1]
        show_result(pred, prob, "Kidney Disease")

# ---------------------- Liver Disease ----------------------
elif disease == "Liver Disease":
    st.header("🫁 Liver Disease Prediction")

    age = st.number_input("Age", 0, 120, 45)
    gender = 1 if st.selectbox("Gender", ["Male", "Female"]) == "Male" else 0
    tb = st.number_input("Total Bilirubin", 0.0, 75.0, 1.0)
    db = st.number_input("Direct Bilirubin", 0.0, 19.0, 0.5)
    alkphos = st.number_input("Alkaline Phosphotase", 0, 2000, 200)
    alt = st.number_input("Alamine Aminotransferase", 0, 2000, 30)
    ast = st.number_input("Aspartate Aminotransferase", 0, 2000, 40)
    tp = st.number_input("Total Proteins", 0.0, 10.0, 6.5)
    alb = st.number_input("Albumin", 0.0, 6.0, 3.3)
    ag = st.number_input("A/G Ratio", 0.0, 3.0, 1.0)

    if st.button("Predict Liver Disease"):
        features = np.array([[age, gender, tb, db, alkphos, alt, ast, tp, alb, ag]])
        pred = liver_model.predict(features)[0]
        prob = liver_model.predict_proba(features)[0][1]
        show_result(pred, prob, "Liver Disease")

# ---------------------- Parkinson's Disease ----------------------
elif disease == "Parkinson’s Disease":
    st.header("🧠 Parkinson’s Disease Prediction")

    fo = st.number_input("MDVP:Fo(Hz)", 0.0, 300.0, 120.0)
    fhi = st.number_input("MDVP:Fhi(Hz)", 0.0, 600.0, 150.0)
    flo = st.number_input("MDVP:Flo(Hz)", 0.0, 300.0, 80.0)
    jitter_percent = st.number_input("MDVP:Jitter(%)", 0.0, 1.0, 0.005)
    jitter_abs = st.number_input("MDVP:Jitter(Abs)", 0.0, 1.0, 0.00005)
    rap = st.number_input("MDVP:RAP", 0.0, 1.0, 0.003)
    ppq = st.number_input("MDVP:PPQ", 0.0, 1.0, 0.003)
    ddp = st.number_input("Jitter:DDP", 0.0, 1.0, 0.009)
    shimmer = st.number_input("MDVP:Shimmer", 0.0, 1.0, 0.03)
    shimmer_db = st.number_input("MDVP:Shimmer(dB)", 0.0, 2.0, 0.3)
    apq3 = st.number_input("Shimmer:APQ3", 0.0, 1.0, 0.02)
    apq5 = st.number_input("Shimmer:APQ5", 0.0, 1.0, 0.03)
    apq = st.number_input("MDVP:APQ", 0.0, 1.0, 0.03)
    dda = st.number_input("Shimmer:DDA", 0.0, 1.0, 0.01)
    nhr = st.number_input("NHR", 0.0, 1.0, 0.02)
    hnr = st.number_input("HNR", 0.0, 50.0, 20.0)
    rpde = st.number_input("RPDE", 0.0, 1.0, 0.45)
    dfa = st.number_input("DFA", 0.0, 1.0, 0.65)
    spread1 = st.number_input("spread1", -10.0, 1.0, -4.0)
    spread2 = st.number_input("spread2", 0.0, 1.0, 0.3)
    d2 = st.number_input("D2", 0.0, 5.0, 2.0)
    ppe = st.number_input("PPE", 0.0, 1.0, 0.2)

    if st.button("Predict Parkinson’s Disease"):
        features = np.array([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                              shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
                              rpde, dfa, spread1, spread2, d2, ppe]])
        pred = parkinson_model.predict(features)[0]
        prob = parkinson_model.predict_proba(features)[0][1]
        show_result(pred, prob, "Parkinson’s Disease")

# Footer
st.markdown("---")
st.caption("Developed for disease prediction with probability & risk levels using trained ML models.")
