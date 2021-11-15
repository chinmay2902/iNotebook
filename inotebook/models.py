from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Notes(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    desc=models.TextField(max_length=8000)
    tags=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)