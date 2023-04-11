#  YATUBE API

## Описание
api для социальной сети yatube.
Через api yatube можно создавать и изменять посты,
подписываться и отписываться от авторов,
получить все свои подписки,
получить список групп или информацию о конкретной группе,
создавать или изменять комментарии к постам.

Используемые утилиты:
- Python 3.9.10
- Django 3.2.16
- djangorestframework 3.12.4

Аутентификация пользователей происходит через JWT-токены.
При получении списка постов есть возможность использовать Limit Offset.
Получить информацию о постах, группах и комментариях,
может любой пользователь, а изменять их только автор.
Получить список своих подписок может только авторизованный пользователь.
Группы изменять можно только в админ панели.


### Установка и запуск
```
python -m venv venv
source venv/Scripts/activate    # WINDOWS
source venv/bin/activate        # linux
pip install -r requirements.txt
cd yatube_api/
python manage.py runserver
```

Примеры запросов:

```
GET
http://127.0.0.1:8000/api/v1/

{
"count": 123,
"next": "http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100",
"previous": "http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100",
"results": [
{
    "text": "string",
    "image": "string",
    "group": 0
}
]
}
```
```
POST
http://127.0.0.1:8000/api/v1/posts/

{
  "text": "string",
  "image": "string",
  "group": 0
}
```
## License

MIT

**Free Software**]()