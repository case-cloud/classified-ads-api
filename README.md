# Classified Ads API

REST API для доски объявлений на FastAPI.

## Что это

Сделала API для доски объявлений, где можно:
- Создавать и управлять объявлениями
- Добавлять категории
- Регистрировать пользователей  
- Искать объявления по фильтрам - цена, категория, город

## На чём написано

- FastAPI — для создания API 
- SQLAlchemy — ORM для работы с базой данных
- SQLite — база данных 
- Pydantic — чтобы проверять данные, которые приходят
- Uvicorn — сервер

## Как запустить

```bash

Здесь я подробно расписала что делает каждое действие:
# Клонирует репозиторий
git clone <ссылка-на-репозиторий>
cd classified-ads-api

# Создает виртуальное окружение
python3 -m venv venv

# Активирует (Mac/Linux)
source venv/bin/activate

# Или Windows:
# venv\Scripts\activate

# Устанавливает всё необходимое
pip install -r requirements.txt

# Запускает сервер
uvicorn app.main:app --reload


## API Endpoints

### Главная
- `GET /` — приветствие

### Категории
- `POST /categories/` — создать категорию
- `GET /categories/` — получить все категории

### Пользователи
- `POST /users/` — создать пользователя
- `GET /users/{user_id}` — получить пользователя

### Объявления
- `POST /ads/` — создать объявление
- `GET /ads/` — получить все объявления с фильтрацией
- `GET /ads/{ad_id}` — получить объявление по ID
- `PUT /ads/{ad_id}` — обновить объявление
- `DELETE /ads/{ad_id}` — удалить объявление

## Примеры

**Создать категорию:**
```json
POST /categories/
{
  "name": "Электроника",
  "slug": "electronics"
}

 ##Создать объявление
POST /ads/
{
  "title": "iPhone 15",
  "description": "Новый телефон",
  "price": 100000,
  "location": "Москва",
  "category_id": 1
}

 ##Структура проекта
classified-ads-api/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
── requirements.txt
├── .gitignore
└── README.md

 ##Важные моменты
База данных SQLite создаётся автоматически (файл classified_ads.db)
Не загружай файл БД на GitHub — он в .gitignore
Виртуальное окружение (venv) тоже не нужно загружать

Автор
Alina Kazieva
