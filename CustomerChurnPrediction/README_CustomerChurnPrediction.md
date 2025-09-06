
# 📊 Customer Churn Prediction

[![GitHub issues](https://img.shields.io/github/issues/LaxmidharPenta/CODSOFT)](https://github.com/LaxmidharPenta/CODSOFT/issues)
[![GitHub forks](https://img.shields.io/github/forks/LaxmidharPenta/CODSOFT)](https://github.com/LaxmidharPenta/CODSOFT/network)
[![GitHub stars](https://img.shields.io/github/stars/LaxmidharPenta/CODSOFT)](https://github.com/LaxmidharPenta/CODSOFT/stargazers)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

---

## 🌟 Project Overview

Customer churn occurs when a customer stops using a company's service.  
This ML project **predicts customer churn** based on customer demographics, account info, and usage patterns.  

**Goal:** Help businesses identify at-risk customers and reduce churn.

---

## 📂 Dataset

- **Dataset:** WA_Fn-UseC_-Telco-Customer-Churn.csv  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- **Target:** `Churn` (Yes = 1, No = 0)  
- **Features:** Demographics, subscription info, services used, charges  

---

## ⚙️ Key Steps

1. **Data Preprocessing**  
   - Drop `customerID`  
   - Convert `TotalCharges` to numeric, fill missing values  
   - Encode categorical columns using `LabelEncoder`  

2. **Train-Test Split & Scaling**  
   - 80% training, 20% testing  
   - Standardize features with `StandardScaler`  

3. **Modeling**  
   - Logistic Regression, Random Forest, XGBoost, etc.  

4. **Evaluation**  
   - Accuracy, Precision, Recall, F1-Score  
   - Confusion Matrix visualization  

---

## 🚀 How to Run

```bash
# Clone repository
git clone https://github.com/LaxmidharPenta/CODSOFT.git
cd CODSOFT/CustomerChurnPrediction

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn

# Run main script
python customer_churn_prediction.py

# Optional: Run Jupyter Notebook
jupyter notebook notebooks/customerchurnprediction.ipynb
```

---

## 📈 Expected Output

- Model metrics: **Accuracy, Precision, Recall, F1-Score**  
- Confusion matrix plots  
- Predictions for new customer data  

---

## 🔮 Future Improvements

- Hyperparameter tuning for better performance  
- Feature importance visualization  
- Deploy as a web application for live predictions  

---

## 🗂️ Project Structure

```
CustomerChurnPrediction/
├─ notebooks/                      
│  └─ customerchurnprediction.ipynb
├─ datasets/                        
│  └─ WA_Fn-UseC_-Telco-Customer-Churn.csv
├─ customer_churn_prediction.py     
├─ README.md                        
```

---

## 🔗 References

- [Kaggle Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)  
- [Analytics Vidhya Churn Prediction Guide](https://www.analyticsvidhya.com/blog/2020/06/customer-churn-prediction-machine-learning/)  

---

## 📝 License

This project is licensed under the **MIT License** – see the [LICENSE](../LICENSE) file in the repository root for details.

**Made with ❤️ by Laxmidhar Penta**
