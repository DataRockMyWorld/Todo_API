from django.db import models

# Create your models here.

# Todo model represents a single todo item
class Todo(models.Model):
    """
    This model holds a single todo item.
    It has three fields:
    - title: A string representing the title of the todo item (max length 120)
    - description: A text field representing the detailed description of the todo item.
    - completed: A boolean field indicating whether the todo item is completed or not.
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
