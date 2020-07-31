from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=128,blank=False)
    is_complete = models.BooleanField(default=False)
    datepublished = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo
     