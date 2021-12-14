from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related


class Card(models.Model):
    color = models.CharField(max_length=200)
    spcolor = models.CharField(max_length=200)
    mood = models.CharField(max_length=200)
    body = models.TextField()
    id = models.CharField(max_length=200,primary_key=True)
    time = models.DateTimeField(auto_now_add=True, null = True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class Meta:
        app_label = "main"
    
    def __str__(self):
        return self.id