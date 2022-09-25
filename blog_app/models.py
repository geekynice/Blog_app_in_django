from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=500)
    date_posted = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        