# Text Sentiment Demo

## 🚀 Overview

This is a **minimal sentiment analysis demo** using **Keras + TensorFlow + FastAPI**.  
It allows you to input a text and predicts whether the sentiment is **Positive** or **Negative**.  

The project is designed for **learning, debugging, and experimenting** with AI models in Python.  
You can run it locally or deploy it on a **VPS using Docker**.

---

## 📂 Project Structure
text-sentiment-demo/ ├─ Dockerfile # Container setup ├─ requirements.txt # Python dependencies ├─ sentiment_model.h5 # Trained Keras model (saved after 
first training) ├─ app.py # FastAPI server └─ templates/
└─ index.html # Minimal landing page for text input

## ⚡ Quick Start (Docker)

1. **Build the Docker image**

```bash
docker build -t sentiment-demo .

2. Run the container
docker run -d -p 8000:8000 sentiment-demo

3. Open your browser and visit:
http://YOUR_VPS_IP:8000


4. Enter text in the form and get instant sentiment predictions.

🛠️ Local Development Make sure you have Python 3.11+ installed. Install dependencies: pip install -r requirements.txt 
Run the FastAPI server:
uvicorn app:app --reload

Model Training The model sentiment_model.h5 is a Keras LSTM model trained on a small demo dataset. To retrain from scratch: python 
create_sentiment_model.py To incrementally train on new data, load the existing model: from tensorflow.keras.models import load_model model = 
load_model("sentiment_model.h5") model.fit(X_new, y_new, epochs=5)
model.save("sentiment_model.h5")

Features Minimal working demo of sentiment analysis Dockerized Python 3 environment (no VPS setup needed) Easy to extend with more data or model 
improvements
Ready for integration into landing pages or web apps

Notes / Tips The .h5 file contains the entire trained model (architecture + weights). Re-running create_sentiment_model.py will overwrite the old .h5 
unless you load it first. Tokenizer must be consistent between training and prediction.
Perfect for learning the AI workflow: train → save → load → predict → deploy.

This project is aimed at: Understanding the full AI pipeline (data → model → deployment) Learning debugging and logging of models Experimenting with model 
optimization
Creating a live demo for learning or presentation


