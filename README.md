# CDN
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

## Примеры запросов

1. Получение информации о добавленных городах GET `/api/cities/` :
   
Ответ:
```
[
    {
        "name": "Москва",
        "latitude": 55.625578,
        "longitude": 37.6063916
    },
    {
        "name": "Питер",
        "latitude": 59.938732,
        "longitude": 30.316229
    },
    {
        "name": "Тверь",
        "latitude": 56.858675,
        "longitude": 35.9208284
    }
[
```

2. Добавление нового города POST `/api/cities/` :

Запрос:  
```
{
    "name":"Нижний Новгород"
}
```

Ответ:
```
{
    "name": "Нижний Новгород",
    "latitude": 58.64912725074507,
    "longitude": 32.06177585476041
}
```

3. Поиск двух ближайших городов по координатам GET `/api/cities/nearest/?latitude=59.7558&longitude=30.6173`

Ответ:
```
[
    {
        "name": "Питер",
        "latitude": 59.938732,
        "longitude": 30.316229
    },
    {
        "name": "Нижний Новгород",
        "latitude": 58.64912725074507,
        "longitude": 32.06177585476041
    }
]
```
