from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='book_covers/')
   



