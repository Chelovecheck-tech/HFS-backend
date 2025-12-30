# Backend (Django) for my-react-app

Минимальный Django-проект с API для управления товарами.

Как запустить (Windows, PowerShell):

1. Перейдите в папку backend:

```powershell
cd backend
```

2. Создайте виртуальное окружение и активируйте его:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

3. Установите зависимости:

```powershell
pip install -r requirements.txt
```

4. Выполните миграции и запустите сервер:

```powershell
python manage.py migrate
python manage.py runserver 8000
```

Добавление изображений (MEDIA)
-------------------------------

В проекте поле `image` в модели `Product` настроено как `ImageField`.
Для работы с загрузкой изображений понадобится библиотека Pillow (она включена в `requirements.txt`).

Файлы будут сохраняться в папке `backend/media/products/` и в режиме разработки Django автоматически отдает их по `MEDIA_URL`.

Если вы используете разработческий сервер, убедитесь, что он запущен и затем загрузите изображение через админку (`/admin/`).

Проверка загруженных изображений:

1. В админке при просмотре продукта появится превью изображения.
2. Файл будет доступен по URL: `http://127.0.0.1:8000/media/products/<filename>`


API endpoints:

- GET /api/products/ — список товаров
- POST /api/products/ — создать товар (ожидает JSON с полями модели, image может быть URL)

Примечания:
- В `shopbackend/settings.py` установлен простой SQLite по умолчанию.
- Для загрузки изображений можно расширить модель и настроить MEDIA_ROOT / MEDIA_URL.
