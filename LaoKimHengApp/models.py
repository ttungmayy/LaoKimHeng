from django.db import models

# Create your models here.

class UserAccount(models.Model):
    id = models.CharField(max_length = 100, primary_key = True)
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)

    def __str__(self):
        return self.id
