# boredapp/models.py
from django.db import models

class ActivitySuggestion(models.Model):
    activity = models.CharField(max_length=255)
    participants = models.PositiveIntegerField()
    activity_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity

    class Meta:
        app_label = 'boredapp'
