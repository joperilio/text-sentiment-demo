import numpy as np

# Trainingsdaten
sentences = [
    "I love this product",
    "This is amazing",
    "I am very happy with the service",
    "What a great experience",
    "I hate this",
    "This is terrible",
    "I am very disappointed",
    "What a bad product"
]
labels = [1, 1, 1, 1, 0, 0, 0, 0]  # 1 = positiv, 0 = negativ

# Tokenizer
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')

# Modell
model = Sequential([
    Embedding(1000, 16, input_length=padded.shape[1]),
    GlobalAveragePooling1D(),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training
model.fit(padded, np.array(labels), epochs=30)

# Modell speichern
model.save('model/sentiment_model.h5')

# Tokenizer speichern
import pickle
with open('model/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Training abgeschlossen und Modell gespeichert!")
