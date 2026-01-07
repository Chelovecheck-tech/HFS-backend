FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Системные зависимости
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python зависимости
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Приложение
COPY . .

# Статика (admin + whitenoise)
RUN python manage.py collectstatic --no-input --clear

# Запуск
CMD ["gunicorn", "shopbackend.wsgi:application", "--bind", "0.0.0.0:8000"]
    