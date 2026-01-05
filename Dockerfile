FROM python:3.11-slim

WORKDIR /app

# Установить зависимости системы
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Скопировать requirements и установить зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать приложение
COPY . .

# Собрать статику
RUN python manage.py collectstatic --no-input --clear

# Запустить приложение
CMD ["gunicorn", "shopbackend.wsgi:application", "--bind", "0.0.0.0:8000"]
