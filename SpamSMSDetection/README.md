📩 Spam SMS Detection using Machine Learning
🔍 Project Overview

This project is an intelligent system that classifies SMS messages as spam (unwanted messages) or ham (legitimate messages).
It leverages Machine Learning with TF-IDF vectorization to convert text messages into numerical features and train models for accurate spam detection.

🎯 Goal: Help users automatically filter unwanted SMS messages.

📂 Dataset

Source: UCI SMS Spam Collection Dataset

File: spam.csv

Columns Used:

v1 → Label (ham or spam)

v2 → SMS message text

Encoding: Latin-1

🗂️ Project Structure
SpamSMS-Detection/
│
├── notebooks/               # Jupyter/Colab notebooks
│   └── exspamsmsdetection.ipynb
├── scripts/                 # Python scripts
│   └── exspamsmsdetection.py
├── data/                    # Dataset
│   └── spam.csv
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

⚡ Features

🧹 Data Preprocessing

Load dataset and clean SMS messages

Encode labels (ham → 0, spam → 1)

📊 Train-Test Split

80% training, 20% testing

Stratified to maintain spam/ham ratio

✏️ Text Vectorization

Convert SMS text into numerical features using TF-IDF

🤖 Machine Learning Models:

Naive Bayes

Logistic Regression

Support Vector Machine (SVM)

📈 Evaluation Metrics:

Accuracy ✅

Classification report 📋

Confusion matrix (visualized with Seaborn) 🟦🟥

💬 Dynamic SMS Testing:

Input new SMS messages and get real-time predictions

⚙️ Installation

Clone the repository:

git clone https://github.com/LaxmidharPenta/CODSOFT.git


Navigate to project folder:

cd CODSOFT/SpamSMS-Detection


Install dependencies:

pip install -r requirements.txt

🚀 How to Use:

Open exspamsmsdetection.ipynb in Jupyter Notebook or Google Colab.

Upload the dataset (spam.csv) if using Colab.

Run all cells sequentially:

Load and explore data 📂

Preprocess and split dataset 🧹

Vectorize messages using TF-IDF ✏️

Train models and evaluate performance 🤖

Test new SMS messages dynamically 💬

🔮 Sample Predictions

Example 1:

Input: "Congratulations! You won a $1000 gift card. Call now!"
Output: Prediction: Spam 📛


Example 2:

Input: "Hey, are we meeting for lunch today?"
Output: Prediction:Not Spam ✅

💡 Future Improvements

Integrate a web interface using Streamlit or Flask 🌐

Use advanced NLP models like LSTM or BERT for higher accuracy 🧠

Deploy as a REST API for mobile or desktop applications 📱💻

📝 License

This project is licensed under the MIT License – see the LICENSE file for details.