from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    # task title. VARCHAR column in SQL DB
    title = models.CharField(max_length=350)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(auto_now=True)  # Viską sutvarkė auto_now=True
    prior = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, editable=False, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.pk:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Task, self).save(*args, **kwargs)
