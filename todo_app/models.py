from django.db import models


class Choices:
    STATUS = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    PRIORITY = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]


class TodoModel(models.Model):
    id = models.UUIDField(editable=False, auto_created=True, unique=True, primary_key=True)
    task = models.CharField(max_length=252, blank=True)
    description = models.CharField(max_length=504, blank=True)
    status = models.CharField(choices=Choices.STATUS, blank=True)
    priority = models.CharField(choices=Choices.PRIORITY, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todo'
        ordering = ['-created_at']
