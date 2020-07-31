from django.db import models

# Create your models here.
class Book(models.Model):
    bookname = models.CharField(max_length=500)
    author   = models.CharField(max_length=500)
    price    = models.IntegerField()
    def __str__(self):
        return self.bookname
