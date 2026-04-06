# Basis-Image: Python 3.11 slim
FROM python:3.11-slim
# Arbeitsverzeichnis im Container
WORKDIR /app
# Abhängigkeiten kopieren
COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt
# Restliche Projektdateien kopieren
COPY . .
# Port freigeben
EXPOSE 8000
# Kommando zum Starten der App
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
