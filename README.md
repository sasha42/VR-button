# VR button for the web
 *hackathon project, probably wont work*

![vr button demo](https://cloud.githubusercontent.com/assets/1775702/18615931/e2b3c090-7db2-11e6-8dcb-8b98f71f8505.gif)


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
