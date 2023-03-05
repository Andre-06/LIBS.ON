from django.db import models
from django.contrib.auth.models import User 

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

#mensagens de erros

class Book(models.Model):
    choices_status = (('V', 'A venda'), ('C', 'Comprado'))

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    telephone = models.CharField(max_length=21)
    tags = models.ManyToManyField(Tag)
    genres = models.ManyToManyField(Genre)
    status = models.CharField(max_length=1, choices=choices_status, default='V')
    photo = models.ImageField(upload_to='fotos_livros')

    def __str__(self):
        return self.name





