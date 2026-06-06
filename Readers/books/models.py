from django.db import models
from django.conf import settings

class Book(models.Model):
    title       = models.CharField(max_length=200)
    author      = models.CharField(max_length=200, default='Unknown Author')
    description = models.TextField(blank=True)
    cover       = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    pages       = models.PositiveIntegerField(blank=True, null=True)
    published   = models.DateField(blank=True, null=True)
    starred_by  = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='starred_books', blank=True)

    def __str__(self):
        return f"{self.title} — {self.author}"