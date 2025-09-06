# ✍️ Handwritten Text Generation using Deep Learning

[![GitHub issues](https://img.shields.io/github/issues/LaxmidharPenta/CODSOFT)](https://github.com/LaxmidharPenta/CODSOFT/issues)
[![GitHub forks](https://img.shields.io/github/forks/LaxmidharPenta/CODSOFT)](https://github.com/LaxmidharPenta/CODSOFT/network)
[![GitHub stars](https://img.shields.io/github/stars/LaxmidharPenta/CODSOFT)](https://github.com/LaxmidharPenta/CODSOFT/stargazers)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

---

## 🔍 Project Overview

This project is a **Deep Learning system** that generates **handwritten-style text** from input text sequences.
It uses **neural networks** and **image processing techniques** to create realistic handwritten characters, useful for documents, notes, or personalized text generation.

**🎯 Goal:** Automatically convert typed text into a **handwritten-style image**.

---

## 📂 Dataset

* **Dataset files:** Fonts and images required for training the model.
* **Example font:** `Zeyada-Regular.ttf`
* **Preprocessing:** Images are converted to grayscale and resized before feeding into the model.

---

## 🗂️ Project Structure

```
HandwrittenTextGeneration/
│
├── notebook/                 # Jupyter/Colab notebooks
│   └── handwrittentextgeneration.ipynb
├── data/                     # Fonts & images for training
│   └── Zeyada-Regular.ttf
└── README_HandwrittenTextGeneration.md  # Project documentation
```

---

## ⚡ Features

1. **🧹 Data Preprocessing**

   * Load and process font images
   * Convert text to grayscale images

2. **🤖 Deep Learning Model**

   * Neural Network trained on handwritten fonts
   * Generates realistic handwritten text from input

3. **💬 Dynamic Text Generation**

   * Input custom text
   * Output handwritten-style image

4. **📈 Evaluation & Visualization**

   * Visual inspection of generated text
   * Adjust model parameters for improved handwriting style

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/LaxmidharPenta/CODSOFT.git

# Navigate to project folder
cd CODSOFT/HandwrittenTextGeneration

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 How to Use

1. Open `handwrittentextgeneration.ipynb` in **Jupyter Notebook** or **Google Colab**.
2. Load fonts and datasets from the `data/` folder.
3. Run all cells sequentially:

   * Preprocess fonts and images 🖼️
   * Train the model 🤖
   * Input text dynamically to generate handwritten images ✍️
4. Save or visualize generated handwriting.

---

## 🔮 Sample Output

**Input:** 
Enter at least 40 characters as seed text:
HI , I am Laxmidhar Penta. This is my Machine Learning project on Handwritten Text Generation.
Using seed text:
 hi , i am laxmidhar penta. this is my ma
**Output:** A realistic handwritten-style image of the text ✍️
<img width="800" height="212" alt="image" src="https://github.com/user-attachments/assets/17613f1c-2441-457d-808e-319617d46177" />


---

## 💡 Future Improvements

* Train on multiple fonts for diverse handwriting styles ✨
* Deploy as a **web app** using Streamlit or Flask 🌐
* Convert output to **PDF or image sequences** for document automation 📄
* Use **GANs** for more realistic handwriting generation 🧠

---

## 📝 License

This project is licensed under the **MIT License** – see the LICENSE file for details.

---

**Made with ❤️ by Laxmidhar Penta**
