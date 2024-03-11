from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    age = models.IntegerField(default = 18)
    gender = models.CharField(max_length = 10, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

