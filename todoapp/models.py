from django.db import models
from django.urls import reverse


class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('todo:todo-list')

    def __str__(self):
        return self.title
