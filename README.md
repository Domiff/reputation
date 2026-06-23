# Reputation API

Backend сервис на Django REST Framework для управления пользователями и системой репутации.

---

## Технологии

- Python 3.14
- Django
- Django REST Framework
- PostgreSQL
- Docker / Docker Compose
- Swagger (drf-spectacular)

---

## Запуск проекта (Docker Compose)

### 1. Клонировать репозиторий

```bash
git clone git@github.com:Domiff/reputation.git
cd <project-folder>
cp .env.template .env
docker compose up --build
```

### 2. Открыть Swagger
После запуска проекта документация API доступна по адресу: http://localhost:8000/schema/swagger-ui/

### 3. Эндпоинты

/api/token - Для получения access токена

/api/profiles/ - Просмотр всех профилей

/api/profiles/{id} - Просмотр конкретного профиля

/api/profiles/current - Просмотр текущего профиля

### 4. Тестовые учетные данные

```json
{
  "username": "admin",
  "password": "123"
}
```
```json
{
  "username": "Bob",
  "password": "123"
}
```
