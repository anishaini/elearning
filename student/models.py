from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notes_filename = models.CharField(max_length=100, null=True, blank=True)  # e.g. "student1_notes.pdf"

    def __str__(self):
        return self.user.username
