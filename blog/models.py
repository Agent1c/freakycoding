from django.db import models
from django.contrib.admin import User

# Create your models here.

class Blog():
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField()
    pass