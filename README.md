# Django Auth + CI Project

## Описание

Простое Django-приложение с системой регистрации, авторизации и защищённой страницей.  
Добавлена автоматическая проверка кода через GitHub Actions.

---

## Функционал

- Регистрация пользователя
- Вход и выход
- Защищённая страница
- Встроенная система Django auth
- Автоматический CI

---

## Технологии

- Python
- Django
- HTML templates
- GitHub Actions
- pytest
- flake8

---

## Запуск проекта

```bash
git clone https://github.com/username/app-auth.git
cd app-auth
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
