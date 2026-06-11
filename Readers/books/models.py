from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    google_books_id = models.CharField(max_length=50, unique=True)
    title           = models.CharField(max_length=500)
    author          = models.CharField(max_length=500, blank=True)
    cover_url       = models.URLField(blank=True, max_length=1000)
    genres          = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return f"{self.title} — {self.author}"


class UserBook(models.Model):
    STATUS_CHOICES = [
        ('want',    'Quiero leer'),
        ('reading', 'Leyendo'),
        ('read',    'Leído'),
    ]

    user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_books')
    book      = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='user_books')
    status    = models.CharField(max_length=10, choices=STATUS_CHOICES)
    rating    = models.PositiveSmallIntegerField(blank=True, null=True)
    read_date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user} — {self.book} ({self.status})"