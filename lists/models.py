from django.db import models

# Create your models here.
class BoookList(models.Model) :
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)

    def __str__(self):
        return self.title