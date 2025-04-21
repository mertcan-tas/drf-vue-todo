from django.db import models
from account.models import User

class Todo(models.Model):
    memo = models.TextField(blank=False)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.memo[:50]  

    class Meta:
        ordering = ['-id']
