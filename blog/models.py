from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from codeon.core.models import ModelBase

# Create your models here.
class Post(ModelBase):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField()
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_view', kwargs={'pk': self.id})

class Comment(ModelBase):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    text = models.TextField()
    post = models.ForeignKey(Post, related_name='comments')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']