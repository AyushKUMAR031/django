from django.db import models

# Create your models here.
# model = database

class Student(models.Model):
     name = models.CharField(max_length=100)
     batch = models.CharField(max_length=10)
     
     def __str__(self):
        return f"{self.name} - {self.batch}"