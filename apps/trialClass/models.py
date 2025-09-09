from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100, 
        validators=[MinLengthValidator(8)],
    )

    def __str__(self):
        return self.username