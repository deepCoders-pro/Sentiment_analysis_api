# devAi430 Sentiment Analysis API 🤖
[![Python](https://img.shields.io/badge/Python-3.8+-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-success)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

## 📘 Overview
The **devAi430 Sentiment Analysis API** is a Python-based web service that performs **sentiment analysis** on text inputs using NLP models.  
It demonstrates **devAi430's** capabilities in integrating AI/ML models into real-world APIs.

---

## 🧠 Features
- RESTful API for real-time text sentiment evaluation  
- Built using **FastAPI** for performance and scalability  
- Modular structure (API, model, utils separated)  
- Ready for Docker deployment or cloud hosting  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/devAi430/devAi430-sentiment-analysis-api.git
cd devAi430-sentiment-analysis-api
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Locally
```bash
uvicorn app.main:app --reload
```
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

---

## 📊 Example Request
```bash
curl -X POST "http://127.0.0.1:8000/predict"      -H "accept: application/json"      -H "Content-Type: application/json"      -d '{"text": "This product is fantastic!"}'
```

**Response:**
```json
{
  "sentiment": "positive",
  "confidence": 0.95
}
```

---

## 🧩 Folder Structure
```
devAi430-sentiment-analysis-api/
│
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── model.py       # Model logic
│   ├── utils.py       # Helper functions
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🧠 Future Enhancements
- Add support for **HuggingFace Transformers**
- Multilingual sentiment support
- Model explainability integration (SHAP/LIME)
- Deploy using Docker + GitHub Actions CI/CD

---

## 🤝 Credits
Originally adapted and branded by **devAi430**  
AI | Automation | Full-Stack | Data Engineering Solutions

---

## 📜 License
This project is licensed under the **MIT License**.  
© 2026 devAi430. All rights reserved.
