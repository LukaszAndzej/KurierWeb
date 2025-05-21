FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalacja narzędzi
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie projektu
COPY . /app/

# Jeśli DEBUG = False w settings.py
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "CourierProject.asgi:application"]
