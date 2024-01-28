# Użyj oficjalnego obrazu Python jako bazowego
FROM python:3.11

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Ustaw zmienne środowiskowe
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Zainstaluj zależności
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Kopiuj projekt
COPY . /app/

# Nadaj skryptowi uprawnienia do wykonania
RUN chmod +x start.sh

# Ustaw polecenie, które będzie uruchamiane podczas startu kontenera
CMD ["./start.sh"]
