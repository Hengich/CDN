# CND
REST-сервис для управления виртуальными серверами.

## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)


### Настройка после клонирования репозитория

После клонирования репозитория устанавливаем и настраиваем виртуальное окружение:

<details>
<summary>
Виртуальное окружение
</summary>

1. Переходим в директорию `CDN_backend`
2. Устанавливаем и активируем виртуальное окружение
    - Для linux/mac:
      ```shell
      python3.11 -m venv venv
      source .venv/bin/activate
      ```
    - Для Windows:
      ```shell
      python -m venv venv
      source venv\Scripts\activate
      ```
    В начале командной строки должно появиться название виртуального окружения `(venv)`
3. Устанавливаем зависимости
    ```shell
    pip install -r requirements.txt
    ```
</details>

## Запуск приложения локально

1. Создайте `.env` на основе файла `envexample`.
2. Примените миграции `python manage.py migrate`
3. Создайте суперпользователя `python manage.py createsuperuser`
4. Запустите сервер `python manage.py runserver`
5. Документация будет доступна по следующим адресам: `/swagger/` и `/redoc/`
