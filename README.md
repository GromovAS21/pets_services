# Сервис для создания информационной базы о породах и собаках
---
Мини приложение на Django для создания создания собак и пород собак с оптимзированными запросами к базе данных

## Основной функционал

- **Создание собаки**
- **Просмотр информации о собаке**
- **Просмотр информации о всех собаках**
- **Изменение информации о собаке**
- **Удаление информации о собаке**
- **Создание породы собаки**
- **Просмотр информации о породе собак**
- **Просмотр информации о всех породах собак**
- **Изменение информации о породе собак**
- **Удаление информации о породах собак**

---

## Технологии и зависимости

### Основные:

- **Python** = "^3.12"
- **Django** = "^5.1.7"
- **Django REST Framework** = "^3.16.0"
- **python-dotenv** = "^1.1.0"
- **psycopg2-binary** = "^2.9.10"
- **gunicorn** = "^23.0.0"

### Для разработки:

- **pre-commit** = "^4.2.0"
- **flake8** = "^7.1.2"
- **isort** = "^6.0.1"
- **black** = "^25.1.0"
- **flake8-docstrings** = "^1.7.0"

---

## Архитектура приложения

### 1. Модели данных

- **Собака (Dog):**
    - Поля:
    - `ID`,
    - `Имя`,
    - `Возраст`,
    - `Порода`,
    - `Пол`,
    - `Цвет`,
    - `Любимая еда`,
    - `Любимая игрушка`

- **Порода (Breed):**
    - Поля:
    - `ID`,
    - `Название`,
    - `Размер`,
    - `Дружелюбность`,
    - `Обучаемость`,
    - `Объем шерсти`,
    - `Требования к физической активности`
  


### 2. Эндпоинты

- **Админ-панель:**
    - `GET admin/` - админ-панель для управления данными    
  
- **Порода:**
    - `GET api/breeds/` — получение списка всех пород собак с добавлением поля **num_dogs** (общее количество собак
      данной породы в бд);
        - Ответ:
          ```
              [
          {
              "id": 1,
              "name": "Хаски",
              "size": "medium",
              "friendliness": 1,
              "trainability": 4,
              "shedding_amount": 5,
              "exercise_needs": 4,
              "num_dogs": 2
          }
          ]
          ``` 
    - `POST api/breeds/` — Создание новой породы собаки в бд;
        - Запрос:
          ```
            {
               "name": "Хаски",
               "size": "medium",
               "friendliness": 1,
               "trainability": 4,
               "shedding_amount": 5,
               "exercise_needs": 4,
            }
          ```

    - `GET api/breeds/<int:pk>/` — получение информации о конкретной породе;
        - Ответ:
          ```
           {
             "id": 1,
             "name": "11",
             "size": "medium",
             "friendliness": 1,
             "trainability": 1,
             "shedding_amount": 1,
             "exercise_needs": 1
           }
          ```
    - `PUT/PATCH api/breeds/<int:pk>/` — изменяет информацию о конкретной породе собак;
    - `DELETE api/breeds/<int:pk>/` — удаляет информацию о конкретной породе собак;

- **Собака:**
    - `GET api/dogs/` — получение списка всех собак с добавлением поля **avg_age** (Средний возраст собак породы данной собаки);
        - Ответ:
          ```
             [
                {
                   "id": 1,
                   "name": "Шарик",
                   "breed": 1,
                   "age": 1,
                   "gender": "male",
                   "color": "black",
                   "favorite_food": null,
                   "favorite_toy": null,
                   "avg_age": 7.0
                }
             ]
          ``` 
    - `POST api/dogs/` — Создание новой собаки в бд;
        - Запрос:
          ```
            {
               "name": "Шарик",
               "breed": 1,
               "age": 1,
               "gender": "male",
               "color": "black",
               "favorite_food": null,
               "favorite_toy": null,
            }
          ```

    - `GET api/dogs/<int:pk>/` — получение информации о конкретной собаке с дополнительным полем **num_same_breed** (Общее количество собак с породой как у конкретной собаки);
        - Ответ:
          ```
           {
             "id": 1,
             "name": "Шарик",
             "breed": 1,
             "age": 13,
             "gender": "male",
             "color": "black",
             "favorite_food": null,
             "favorite_toy": null,
             "num_same_breed": 2
           }
          ```
    - `PUT/PATCH api/dogs/<int:pk>/` — изменяет информацию о конкретной собаке;
    - `DELETE api/dogs/<int:pk>/` — удаляет информацию о конкретной собаке;

---

## Установка и запуск

### 1. Клонирование репозитория
   ```bash
   git clone https://github.com/GromovAS21/em_homework_3.git
   cd em_homework_3
   ```
### 2. Установка зависимостей

- Установите зависимости с помощью Poetry и активируйте виртуальное окружение:
    ```bash
    poetry install
    poetry shell
    ```

### 3. Настройка переменных окружения

- Переименуйте файл [.env.sample](.env.sample) в [.env](.env.sample) и заполните все переменные в этом файле.


### 4. Запуск приложения

   - Запуск через Docker (веб-сервис)
       ```bash
       docker-compose up -d --build
       ```
     _Веб-приложение будет доступно по адресу: http://127.0.0.1_

---

## Pre-commit (Для разработки)

В проекте присутствует функция pre-commit, который проверяет код на соответствие стандартам PEP8 состоящие из `isort`,
`black`, `flake8`, `flake8-docstrings`;

### Запуск Pre-commit

```bash
pre-commit install
git add .pre-commit-config.yaml
```

После этого при попытке создания коммита будет запускаться проверка кода и если все проверки проходят, создается коммит.

Для ручной проверки кода необходимо выполнить команду:

```bash
pre-commit run --all-files
```

#### ВАЖНО!!! ####

Перед коммитом необходимо выполнить одну из следующих команд:

```bash
git add . # Добавляет все файлы в индекс
```

```bash
git add <file_name> # Добавляет указанный файл в индекс
```

---

## Цитата

> "Если над кодом работали 20 человек, значит его можно сделать в 20 раз меньше и в 20 раз быстрее"* - Бьёрн Страуструп

---

Приятного использования! 🚀
