# VR button for the web
* This is a work in progress *

This is a button that can injected on any page which enables a VR Cardboard view in modern browsers. Works best for mobile.

## Running
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# go to http://localhost:8000/admin
# login
# add buttons
# then you can view buttons on:
# http://localhost:8000/button/<id>
```
