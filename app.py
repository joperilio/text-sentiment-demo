from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = FastAPI()

# Modell und Tokenizer laden
model = tf.keras.models.load_model('model/sentiment_model.h5')
with open('model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

class TextData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to the Text Sentiment Analysis API!"}

@app.post("/predict/")
def predict_sentiment(data: TextData):
    text = data.text
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=10, padding='post')
    prediction = model.predict(padded)[0][0]
    sentiment = "positive" if prediction > 0.5 else "negative"
    return {"sentiment": sentiment, "confidence": float(prediction)}
