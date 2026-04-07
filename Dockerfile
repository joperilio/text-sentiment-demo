# Vollständiges Python 3.11 Image (nicht slim)
FROM python:3.11

# Arbeitsverzeichnis im Container
WORKDIR /app

# Systempakete, inkl. curl, git, build tools
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Kopiere Abhängigkeiten
COPY requirements.txt .

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere Projektdateien
COPY . .

# Expose FastAPI Port
EXPOSE 8000

# Default Command für Entwicklungsmodus (Container bleibt offen)
CMD ["tail", "-f", "/dev/null"]
