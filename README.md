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
docker build -t python3-dev .

2. Run the container
#d ocker run -d -p 8000:8000 python3-dev
docker run -d -v $(pwd):/app -p 8000:8000 --name python3-dev python3-dev     uvicorn app:app --host 0.0.0.0 --port 8000 --reload

you can run as well, docker run -d --name python3-dev   -v $(pwd):/app -w /app   -p 8000:8000   python3-dev tail -f /dev/null
 -- >to map to you local code base with this -v $(pwd):/app - it means local changes will be loaded on restart of the container (docker restart python.dev).
With this, the container is staying running as daemon and not terminating immediately. you might want 

Pay attention that python3 packages must importes as in requirments.txt, we use a full paython image whcih contains already the packages, or use pip to install them

Starting FastAPI im Container: uvicorn app:app --host 0.0.0.0 --port 8000 (it will be started by Dockerfile, but might be usefull)

Creating the model in the cnotainer, from outside with:  sudo docker exec -it python3-dev python3 create_sentiment_model.py 

3. Open your browser and visit:
http://YOUR_VPS_IP_or_Any_Remote_IP_Where_Container_Runs:8000


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


Testing samples:
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"text":"I love this project!"}'
