# minimum_django

## what have I runed:
```
django-admin startproject mysite
python manage.py startapp polls
```

edit :
urls.py -> include polls
polls/urls.py -> add pattern 
polls/view.py -> get template (index.html)
settings.py -> installed_app add polls


bash:
python manager.py runserver 

on web_broswer:
http://127.0.0.1:8000/polls/
(ip you assign)
