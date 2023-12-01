from django.db import models
from users.models import User

# Create your models here.
class Question(models.Model):

    ANSWER_TYPES = [
        ('yes_no', 'Yes/No'),
        ('number', 'Number'),
        ('text', 'Text'),
    ]

    code = models.CharField(max_length=10)
    content = models.TextField()
    kpi = models.CharField(max_length=100)
    answer_type = models.CharField(max_length=20, choices=ANSWER_TYPES)
    answer = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')

