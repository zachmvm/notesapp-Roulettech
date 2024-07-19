from django.db import models
from django.contrib.auth.models import User

# Models 
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Auto generate new time stamp for each note
    created_at = models.DateTimeField(auto_now_add=True)
    # Specify who made note
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    # Above ^ code ^ references User, and on delete will remove all associated notes with that user
    def __str__(self):
        return self.title