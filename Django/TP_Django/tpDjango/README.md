#Django Quickstart

`python3 -m django --version`

Créer un projet Django:  
`django-admin startproject name_project`

Lancer le serveur de dev:   
`python3 manage.py runserver`

Create an app inside the new project:  
`python3 manage.py startapp name_application`



Add the new app in settings.py  

```python
INSTALLED_APPS = [
    ...,
    'toDoList.apps.TodolistConfig',  
]
```

Add Urls files in name_application
`touch name_application/urls.py`

Add urls form name_application inside name_project/name_project/urls.py:  
`path('todolist/', include('toDoList.urls')),`



Create Model :   
```python
class Task(models.Model):
    content = models.CharField(max_length=255),
    is_done = models.BooleanField,
    created_date = models.DateTimeField('date created')
```
  
`python3 manage.py migrate`
`python manage.py makemigrations polls`
