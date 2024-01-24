# Django Notes

## Running the server

You can run the Django development server on a custom host and port or tell Django to load a specific settings file, as follows:

> > > python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings

## installing all the requirements

> > > pip install -r requirements.txt.

## The settings file

1. DEBUG is a Boolean that turns the debug mode of the project on and off. If it is set to True, Django will display detailed error pages when an uncaught exception is thrown by your application.When you move to a production environment, remember that you have to set it to False.
2. ALLOWED_HOSTS is not applied while debug mode is on or when the tests are run. Once you move your site to production and set DEBUG to False, you will have to add your domain/host to this setting to allow it to serve your Django site.
3. INSTALLED_APPS is a setting you will have to edit for all projects. This setting tells Django which applications are active for this site.
4. MIDDLEWARE is a list that contains middleware to be executed.
5. ROOT_URLCONF indicates the Python module where the root URL patterns of your application are defined.
6. DATABASES is a dictionary that contains the settings for all the databases to be used in the project.
7. LANGUAGE_CODE defines the default language code for this Django site.
8. USE_TZ tells Django to activate/deactivate timezone support.

## What is a slug

```python

class Post(models.Model):
    title = models.CharField(max_legth = 250)
    slug = models.SlugField(max_length = 250)
    body = models.TextField()

    def __str__(self):
        return self.title
```

slug: This is a SlugField field that translates into a VARCHAR column in the SQL database. A slug is a short label that contains only letters, numbers, underscores, or hyphens. A post with the title "Django Reinhardt: A legend of Jazz" could have a slug like "django-reinhardt-legend-jazz". We will use the slug field to build beautiful, SEO-friendly URLs for the blog posts.

## {% load static %}

{% load static %} tells Django to load the static template tags that are provided by the django.contrib.staticfiles application, which is contained in the INSTALLED_APPS setting. After loading them, you can use the {% static %} template tag throughout this template. With this template tag, you can include the static files, such as the blog.css file, which you will find in the code of this example under the static/ directory of the blog application.

page 87
