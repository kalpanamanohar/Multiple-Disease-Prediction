# 📌 Multiple Disease Prediction System

A machine-learning powered web application that predicts the likelihood of multiple diseases (Kidney disease, Liver disease, Parkinson’s, etc.) based on user-provided medical inputs.  
The project integrates ML models with a user-friendly Streamlit interface for quick, accessible health insights.

---

## 🚀 Project Objective

- Assist in early detection of diseases  
- Improve decision-making for healthcare providers  
- Reduce diagnostic time & cost through fast predictions  
- Build a system that is scalable, accurate, and easy to use  

---

## 🧱 System Architecture

### 1. Frontend
- Built using **Streamlit**
- Accepts user input such as symptoms, test results, demographic details

### 2. Backend
- Python-based preprocessing
- Model inference and result generation

### 3. Machine Learning Models
- Logistic Regression  
- Random Forest  
- XGBoost  
- Individual models for each disease OR multi-output classifier

---

## ✨ Features

- 🔍 Predicts multiple diseases (Kidney, Liver, Parkinson’s, etc.)  
- 🧑‍💻 Simple and intuitive Streamlit UI  
- 📊 Interactive graphs and results visualization  
- 🔐 Secure data handling  
- 📈 Scalable for adding new disease models  

---

## 🔄 Workflow Overview

1. **User Input:** Symptoms, medical test values, demographics  
2. **Data Preprocessing:**  
   - Missing value handling  
   - Categorical encoding  
   - Feature scaling  
3. **Model Prediction:**  
   ML models compute probabilities and return disease risk  
4. **Output:**  
   - Displays predicted disease  
   - Shows confidence score  

---

## 🛠 Implementation Details

### 📁 Data Collection
Datasets used:
- Parkinson’s dataset  
- Kidney disease dataset  
- Indian liver patient dataset  

### ⚙ Data Preprocessing
- Handling missing values  
- One-hot encoding  
- MinMax / Standard scaling  

### 🤖 Model Training
- Separate classifiers trained for each disease  
- Cross-validation applied  

### 📊 Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  
- ROC-AUC  

---

## 🧪 Tools & Technologies

| Category | Technologies |
|---------|--------------|
| Programming | Python |
| ML Libraries | Scikit-learn, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| UI Framework | Streamlit |

---

## 📍 Results
The system provides accurate predictions for multiple diseases and enhances early detection. The interactive UI improves accessibility for users and healthcare practitioners.

---

## 📏 Evaluation Metrics Used

### Classification
- Accuracy  
- Precision, Recall, F1-score  

### Application Quality
- Response time  
- Visual clarity  

---

## 🏷 Tags
`Machine Learning` `Streamlit` `Prediction App` `Python` `Classification Models`

---

## 📦 Project Deliverables

- Python ML scripts  
- Trained ML models  
- Streamlit UI application  
- Documentation & explanation workflow  

---

## ▶️ How to Run the Project

```bash
# 1. Clone the repository
git clone https://github.com/kalpanamanohar/multiple-disease-prediction.git
cd multiple-disease-prediction

# 2. Install required packages
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
