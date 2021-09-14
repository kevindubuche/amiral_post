1. create code directory
2. python3 -m venv venv
3. source venv/bin/activate
4. install dependencies
pip install django
pip install django-summernote
python -m pip install Pillow
5. django-admin startproject amiral_post .
6. python manage.py startapp blog
7. in blog, create the directory templates/blog
8. in amiral_post/setting.py add blog in INSTALLED_APP
9. Create the models
11. python3 manage.py makemigrations
12. python3 manage.py migrate
13. python3 manage.py createsuperuser
14. python3 manage.py runserver
15. pipreqs
--------------HEROKU---------------
1. Create procfile
2. in seetings set DEBUG to Fasle