from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo= models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Breakfast(models.Model):
    name = models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    # 'todo/static/breakfasts'
    image=models.FileField(upload_to='images/', blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
