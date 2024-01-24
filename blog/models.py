from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

""" 
We can access "Post.Status.choices" to obtain the available choices
[('DF', 'Draft'), ('PB', 'Published')], 
"Post.Status.labels" to obtain the human-readable names
['Draft', 'Published'],
"Post.Status.values" to obtain the actual values of the choices
['DF', 'PB'],
"Post.Status.names" to obtain the names of the choices
['DRAFT', 'PUBLISHED'].

We use related_name to specify the name of the reverse relationship, from User to Post.
This will allow us to access related objects easily from a user object by using the user.blog_posts notation. 
"""

#A manage that returns all the published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now =True)
    created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=2, choices=Status.choices, default= Status.DRAFT)
    
    #default manager
    objects = models.Manager()
    #custom
    published = PublishedManager()
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args = [
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
            ])