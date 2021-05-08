from django.db import models

class Contract(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    descp = models.CharField(max_length=122)
    rating = models.CharField(max_length=122)
    avtar = models.CharField(max_length=122)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    