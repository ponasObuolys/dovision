from django.db import models

# Create your models here.


class Task(models.Model):
    # task title. VARCHAR column in SQL DB
    title = models.CharField(max_length=350)
    # is task completed or not
    completed = models.BooleanField(default=False)
    # automatic datetime upon task creation
    created = models.DateTimeField(auto_now_add=True)
    # no primary key as Django model creates it automatically
    priority = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.title


class TodoList(models.Model):
    text = models.CharField(max_length=350)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
