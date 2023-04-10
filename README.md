#  YATUBE API

## api для социальной сети yatube

### Установка и запуск
необходим python версии 3.9.10
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

**Free Software**