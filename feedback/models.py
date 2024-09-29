from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True)  # Optioneel als je anonieme feedback toestaat
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'} on {self.created_at}"
