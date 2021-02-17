from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    # task title. VARCHAR column in SQL DB
    title = models.CharField(max_length=350)
    # is task completed or not
    completed = models.BooleanField(default=False)
    # automatic datetime upon task creation
    created = models.DateTimeField(editable=False)
    # modified = models.DateTimeField(editable=False)
    # no primary key as Django model creates it automatically
    # priority = models.PositiveIntegerField(blank=True, default=0)
    # ?????
    prior = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.pk:
            self.created = timezone.now()
            self.modified = timezone.now()
        return super(Task, self).save(*args, **kwargs)


class TodoList(models.Model):
    text = models.CharField(max_length=350)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
