from django.db import models
from django.conf import settings

class Book(models.Model):
    google_books_id = models.CharField(max_length=50, unique=True)
    title           = models.CharField(max_length=200)
    author          = models.CharField(max_length=200, blank=True)
    cover_url       = models.URLField(blank=True)
    starred_by      = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='starred_books', blank=True)

    def __str__(self):
        return f"{self.title} — {self.author}"