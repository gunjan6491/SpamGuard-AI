# SpamGuard AI 📩

**An Intelligent SMS Spam Detection Web Application using Machine Learning and NLP.**

SpamGuard AI is a web-based application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing and Machine Learning.

The project compares three machine learning algorithms with two text vectorization techniques to explore different approaches to SMS spam detection.

## 🚀 Features

- Detects whether an SMS message is Spam or Ham.
- Supports three Machine Learning algorithms.
- Supports Bag of Words (BoW) and TF-IDF vectorization.
- Performs text preprocessing before prediction.
- Uses additional text-based features for classification.
- Interactive web interface built using Flask, HTML, CSS, and JavaScript.

## 🧠 Machine Learning Models

The application supports six model configurations:

| Algorithm | Vectorization |
|---|---|
| Naive Bayes | Bag of Words |
| Random Forest | Bag of Words |
| Logistic Regression | Bag of Words |
| Naive Bayes | TF-IDF |
| Random Forest | TF-IDF |
| Logistic Regression | TF-IDF |

## 🛠️ Technologies Used

- **Programming:** Python
- **Machine Learning:** Scikit-learn
- **NLP:** Text Preprocessing, Bag of Words, TF-IDF
- **Data Analysis:** Pandas, NumPy
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Model Persistence:** Joblib

## 📂 Project Structure

```text
SpamGuard-AI/
│
├── app.py
├── preprocessing.py
├── requirements.txt
│
├── model/
│   ├── naive_bayes.pkl
│   ├── random_forest.pkl
│   ├── logestic.pkl
│   ├── naive_bayes2.pkl
│   ├── random_forest2.pkl
│   └── logistic2.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/SpamGuard-AI.git
```

### 2. Navigate to the project directory

```bash
cd SpamGuard-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 🔍 How It Works

1. User enters an SMS message.
2. Text preprocessing cleans and transforms the message.
3. Additional features such as word count, character count, digits, and special characters are extracted.
4. The selected Machine Learning model processes the input.
5. The application predicts whether the message is Spam or Ham.
6. The result is displayed on the web interface.

## 🎯 Project Objective

The main objective of SpamGuard AI is to build an interactive SMS spam detection system and compare different combinations of machine learning algorithms and text vectorization techniques.

## 👩‍💻 Author

**Gunjan Aswani**

B.Tech – Artificial Intelligence & Machine Learning


---

⭐ If you find this project interesting, consider giving it a star!
