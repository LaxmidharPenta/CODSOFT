TASK 1:
📩 Spam SMS Detection using Machine Learning
🔍 Project Overview

This project is an intelligent system that classifies SMS messages as spam (unwanted messages) or ham (legitimate messages).
It uses Machine Learning with TF-IDF vectorization to convert SMS text into numeric features and train models for accurate spam detection.

🎯 Goal: Help users automatically filter unwanted SMS messages.

📂 Dataset

Source: UCI SMS Spam Collection Dataset

File: spam.csv

Columns:

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

1. 🧹 Data Preprocessing

  Load dataset and clean SMS messages

  Encode labels (ham → 0, spam → 1)

2. 📊 Train-Test Split

  80% training, 20% testing

  Stratified to maintain spam/ham ratio

3. ✏️ Text Vectorization

  Convert SMS text into numeric features using TF-IDF

4. 🤖 Machine Learning Models

  Naive Bayes

  Logistic Regression

  Support Vector Machine (SVM)

5. 📈 Evaluation

  Accuracy ✅

  Classification report 📋

  Confusion matrix (visualized with Seaborn) 🟦🟥

6. 💬 Dynamic SMS Testing

  Input new SMS messages and get real-time predictions

⚙️ Installation

1. Clone the repository:

git clone https://github.com/LaxmidharPenta/CODSOFT.git

2. Navigate to project folder:

cd CODSOFT/SpamSMS-Detection


3. Install dependencies:

pip install -r requirements.txt

🚀 How to Use

1. Open exspamsmsdetection.ipynb in Jupyter Notebook or Google Colab.

2. Upload the dataset (spam.csv) if using Colab.

3. Run all cells sequentially:

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
Output: Prediction: Ham ✅

💡 Future Improvements

Integrate a web interface using Streamlit or Flask 🌐

Use advanced NLP models like LSTM or BERT for higher accuracy 🧠

Deploy as a REST API for mobile or desktop applications 📱💻

📝 License

This project is licensed under the MIT License – see the LICENSE file for details.
