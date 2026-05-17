from django.db import models
from users.models import User
from django.contrib.auth import get_user_model



# Create your models here.

User = get_user_model()
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    tasksfield = models.CharField(max_length = 64)
    description= models.CharField(max_length = 256)
    completed = models.CharField(max_length = 10, default="")
    
    def __str__(self):
        return f"{self.tasksfield}  {self.description} {self.completed}"
    
