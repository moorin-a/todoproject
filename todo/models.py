from django.db import models

# Create your models here.

CHOICE = (('danger', 'job'), ('warning', 'house-work'), ('primary', 'self-study'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = CHOICE
    )
    duadate = models.DateField()

    def __str__(self):
        return self.title


