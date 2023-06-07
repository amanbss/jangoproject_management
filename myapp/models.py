from django.db import models

# Create your models here.
class query(models.Model):
    name=models.CharField(max_length=200)
    password=models.IntegerField()
    def __str__(self):
        return self.name