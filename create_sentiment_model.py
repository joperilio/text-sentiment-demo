from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import os
# 📦 Trainingsdaten (~100 Beispiele)
texts = [
# POSITIV
"I love this product",
"This is amazing",
"Absolutely fantastic",
"I really like it",
"Great work",
"This is wonderful",
"I enjoy using this",
"Very good experience",
"I am happy with this",
"This works perfectly",
"Excellent quality",
"I highly recommend it",
"Sogood",
"I like this a lot",
"This is very nice",
"Brilliant idea",
"I am impressed",
"Superb performance",
"Very satisfied",
"This is awesome",
"I love this project",
"Everything is great",
"It works great",
"Really good",
"Very useful",
"Nice and clean",
"Good job",
"I appreciate this",
"This is perfect",
"Outstanding work",
"I love how this works",
"Very reliable",
"I am very pleased",
"This makes me happy",
"Incredible result", 
"Top quality",
"I like the design",
"This is very helpful",
"Best experience",
"I love using this",
"Everything works well",
"This is excellent",
"I enjoy this a lot",
"Fantastic job",
"Really impressive",
"Great experience",
"Very cool","I am satisfied",
"This is brilliant",
# NEGATIV
"I hate this product",
"This is bad",
"Very disappointing",
"I don't like it",
"Terrible experience",
"This is awful",
"I am unhappy",
"Worst ever",
"Not good",
"This is not working",
"Very bad quality",
"I regret using this",
"So bad",
"I dislike this",
"This is horrible",
"Really poor",
"I am frustrated",
"Very annoying",
"Completely useless",
"This is terrible", 
"I hate this project",
"Everything is broken",
"It does not work",
"Really bad",
"Very slow",
"Bad experience",
"I am not satisfied",
"This is wrong",
"Poor performance",
"I don't recommend it", 
"Very unreliable",
"I am disappointed",
"This makes me angry",
"Awful result",
"Low quality",
"I hate how this works",
"This is not helpful",
"Worst experience",
"I don't enjoy this",
"Everything fails",
"This is disappointing",
"I dislike using this",
"Terrible job",
"Really frustrating",
"Bad design", 
"I am upset",
"This is useless",
"Very poor",
"I don't like this at all" ]

labels = [1]*49 + [0]*49 # 1=positiv, 0=negativ


# -------------------------------
# 2️⃣ Tokenizer erstellen
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)


# 🔢 Text → Zahlen
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=10, padding='post')

# 🧠 Modell
model = Sequential()
model.add(Embedding(input_dim=1000, output_dim=16))
model.add(LSTM(16))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 🚀 Training
model.fit(padded, np.array(labels), epochs=20, verbose=1)

# 📁 Ordner sicherstellen
os.makedirs("model", exist_ok=True)

# 💾 Modell speichern
model.save("model/sentiment_model.h5")

# 💾 Tokenizer speichern
with open("model/tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("✅ Model und Tokenizer gespeichert!")
