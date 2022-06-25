from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text='Breve descrição da obra'
    )
    isbn = models.CharField('ISBN', max_length=11)
    genre = models.ManyToManyField(
        Genre, help_text='Selecione um gênero literário'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': str(self.pk)})
