
# Cyfrowa szkoła sukcesu
![Demo](http://i.imgur.com/DvO0CaF.gif)

Visit website at <http://cyfrowa-szkola.eu>

VEDIUS branch is avaible at <http://cyfrowa-szkola.net>

In the feature, this two branches will be marged into one, main project.

Django application which allows multiple users (students) to share their projects and create their online portfolio.

Using Social Accounts validation (allauth - Google, Facebook and local accounts), CKEditor for modyfing projects content and more.


## Requirements


`pip install -r requirements.txt`

`npm install`

* gulp-cli
* gulp
* gulp-sass
* gulp-autoprefixer

`gulp build`

## Configuration


To configure Facebook and Google authentication generate ID's and secret keys.

* Google - <https://developers.google.com/identity/sign-in/web/devconsole-project>
* Facebook - <http://developers.facebook.com>

To configure ReCaptcha:
* Get a public key and private key from <https://www.google.com/recaptcha/intro/index.html>
* Add following lines to `settings.py`:
    
        RECAPTCHA_PUBLIC_KEY = 'MyRecaptchaKey123'
        RECAPTCHA_PRIVATE_KEY = 'MyRecaptchaPrivateKey456'

* Wherever you need a Captcha, add a field to the form:
    
        from captcha.fields import ReCaptchaField
        captcha = ReCaptchaField()

Admin panel

* Sites - remove example, add your site
* Social Applications - add social ID's, Key's and relate to site


## What we are using

* Django allauth <https://github.com/pennersr/django-allauth>
* Django ckeditor <https://github.com/django-ckeditor/django-ckeditor>

## Static files

Static files root is static_cdn to generate them:

` python manage.py collectstatic `


## Project URL's

projects/ - list of uers with projects

 * /user/id - user detail (with his projects)
 * /slug - project detail
 * /create - create project
 * /slug/edit - edit project


