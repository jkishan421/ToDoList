from django.db import models
from model_utils import Choices
from django.utils import timezone


class ToDoList(models.Model):
    STATUS_CHOICES = Choices(
        'Pending',
        'Completed',
        'Overdue',
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES.Pending, max_length=10)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
