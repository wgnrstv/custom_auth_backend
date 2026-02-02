# Custom Authentication & Authorization System

Тестовое задание: реализация собственной системы управления доступом (RBAC) на Django + DRF.

## 1. Особенности реализации
- **Custom User Model**: Аутентификация по `email` вместо `username`.
- **Soft Delete**: "Мягкое" удаление пользователей (`is_active=False`) — данные сохраняются в базе, но доступ блокируется.
- **Собственная система RBAC**: 
    - Доступ не зависит от встроенных групп Django.
    - Реализована структура: **User ↔ Role ↔ AccessRule ↔ Resource**.
    - Доступ проверяется через кастомный класс `HasResourcePermission`.

## 2. Схема базы данных (Авторизация)
1. **Resource**: Список защищаемых объектов (например, `FinancialData`).
2. **Role**: Роли пользователей (например, `Manager`).
3. **AccessRule**: Связующая таблица. Определяет, какая роль имеет доступ к конкретному ресурсу с определенным правом (`view`, `edit`, `delete`).

## 3. API Эндпоинты
- `POST /api/register/` — Регистрация.
- `POST /api/login/` — Получение JWT-токена.
- `GET/PUT/DELETE /api/profile/` — Управление профилем (включая Soft Delete).
- `GET /api/business-data/` — Mock-ресурс (требует роль с доступом к `FinancialData`).

## 4. Запуск проекта
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
2. Примените миграции:
   ```bash
python manage.py migrate

3. Запустите сервер:
   ```bash
python manage.py runserver

## Данные для тестирования (Суперпользователь)
Для проверки системы и доступа в админ-панель:
- **Email**: custom@mail.ru
- **Пароль**: 12345678

Эти данные позволяют:
1. Зайти в `http://127.0.0.1`.
2. Управлять ролями и правилами доступа.
3. Получить JWT-токен через `/api/login/