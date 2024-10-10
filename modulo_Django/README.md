### MÓDULO DE DJANGO

Para rodar o projeto da aula:

```
py -m venv venv
.\venv\Scripts\activate
pip freeze > requirements.txt
pip install -r requirements.txt

django-admin startproject setup .
py .\manage.py runserver

django-admin startapp sistema
```