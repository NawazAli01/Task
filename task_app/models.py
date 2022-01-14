from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Id = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['Id']

    def __str__(self):
        return self.first_name
