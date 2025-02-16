# 🔍 Churn Modelling Prediction

## 🚀 Overview
Churn Modelling is a **machine learning project** that predicts whether a customer is likely to leave a bank (churn) based on their demographic and financial data.  
The model is powered by **FastAPI**, with an interactive **web UI** for user-friendly predictions.  

## 📊 Dataset Information
The model is trained on a **customer churn dataset** containing various demographic, financial, and account-related features.  

- **Dataset Name:** Bank Customer Churn Dataset  
- **Number of Samples:** 10,000 customers  
- **Number of Features:** 14  
- **Target Variable:** `Exited` (1 = Churned, 0 = Not Churned)  

### **🔹 Key Features**
| Feature         | Description |
|----------------|-------------|
| `CustomerId`   | Unique identifier for each customer |
| `Surname`      | Customer's last name |
| `CreditScore`  | Customer's credit score (0-1000) |
| `Geography`    | Country of residence (`France`, `Spain`, `Germany`) |
| `Gender`       | Customer’s gender (`Male`, `Female`) |
| `Age`          | Age of the customer |
| `Balance`      | Account balance (in USD) |
| `NumOfProducts`| Number of products held with the bank |
| `IsActiveMember` | Whether the customer is an active member (1 = Yes, 0 = No) |
| `Exited`       | Target variable (1 = Churned, 0 = Not Churned) |

## 🎯 Features
- ✅ **FastAPI-powered REST API** for churn prediction
- ✅ **Secure API authentication** using API keys  
- ✅ **Machine learning model trained on customer data**  
- ✅ **User-friendly web interface** with real-time validation  
- ✅ **Dropdowns & placeholders for an intuitive experience**  
- ✅ **Detailed error messages & formatted predictions**  

## 🛠 Tech Stack
- **Backend:** FastAPI, Python  
- **Machine Learning:** Scikit-Learn, XGBoost  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Git, GitHub, Uvicorn  

---

## ⚙️ Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/asmaa-2ahmed/Churn-Modelling.git
cd Churn-Modelling
```

### **2️⃣ Set Up a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add:
```ini
APP_NAME="Churn Modelling"
VERSION="1.0.0"
API_SECRET_KEY="your_api_key_here"
```

### **5️⃣ Run the API**
```sh
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
API will be available at **http://127.0.0.1:8000** 🚀  

---

## 📡 API Endpoints

| **Method** | **Endpoint**            | **Description** |
|-----------|------------------------|----------------|
| `GET`     | `/`                    | Check API status |
| `POST`    | `/predict/forest`       | Predict customer churn |

**Example Request:**
```json
{
    "CreditScore": 619,
    "Geography": "France",
    "Gender": "Female",
    "Age": 42,
    "Balance": 50000.0,
    "NumOfProducts": 2,
    "IsActiveMember": 1
}
```

**Example Response:**
```json
{
    "churn_prediction": true,
    "churn_probability": 0.62
}
```

---

## 🌐 Web UI Preview
![Churn UI](https://via.placeholder.com/800x400?text=Churn+Prediction+UI)  
The **web interface** allows users to enter details and predict churn directly from the browser.

---

## 🤝 Contributors
- **Asmaa Ahmed** - [GitHub](https://github.com/asmaa-2ahmed)  
- **You!** Feel free to contribute! 🚀  

## 📝 License
This project is licensed under the **MIT License**.

---

## ⭐ Show Your Support!
If you like this project, please **give it a star ⭐😊**   
```

