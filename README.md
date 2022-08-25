This is a guide to help streamline the proccess of setting up a new website using django that I made for myself.
Following this guideline will setup a basic website with a homepage, and a basic user signup, login, and authentication system.

Steps:
1. Setup virtual env for your project
2. Install django using command $python -m pip install django~=4.0.0
3. Make migrations for admin and user accounts $python manage.py makemigrations accounts
                                               $python manage.py migrate
4. Make superuser for admin on website $python manage.py createsuperuser 
5. Install crispyforms $python -m pip install django-crispy-forms==1.13.0
                       $python -m pip install crispy-bootstrap5==0.6
6. Install environs $python -m pip install 'environs[django]==9.3.5'
7. Create .env file for storing environment variables 
8. Add DEBUG = True to .env
9. Add SECRET_KEY = generated_password_here to .env using a generated secret key from $python -c "import secrets"; print(secrets.token_urlsafe())"
10. Add DATABASE_URL = sqlite:///db.sqlite3   to .env
11. Install Psycopg $python -m pip install psycopg2==2.9.3
12. Install whitenoise $python -m pip install whitenoise==5.3.0
13. Run collect static $python manage.py collectstatic 
14. Install gunicorn $python -m pip install gunicorn==20.1.0

Now you should have the basis of website that can run on your local environment! 
For further steps, I would recommend setting up an email service that can help users reset passwords with sendgrid.
Then, I would further set up permissions and authorizations so that users that aren't logged in are restricted on what they can access.
Finally, you can delpoy your website using a service such as heroku. 

This guide was created using the help of the excellent book django for beginners, be sure to check it out! 
