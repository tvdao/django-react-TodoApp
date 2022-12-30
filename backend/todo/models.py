from django.db import models
import datetime
# Create your models here.

class Todo(models.Model):
    created = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title