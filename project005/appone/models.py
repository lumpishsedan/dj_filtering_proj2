# app/models.py
from django.db import models
from django.urls import reverse # new

class Post(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text[:50]
    keyone = models.IntegerField(default = '777')

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])
