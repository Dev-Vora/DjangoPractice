from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cno  = models.CharField("Contact Number", max_length=12)
    desc = models.TextField("Description")
    date = models.DateField()
    def __str__(self):
        return self.name
    