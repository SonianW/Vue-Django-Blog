from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    author = models.ForeignKey(User, 
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self) -> str:
        return self.title