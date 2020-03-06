from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A single Blog post
    """
    user = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.user