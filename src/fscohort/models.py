from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.firstName, self.lastName, self.number)

    

# Create your models here.
