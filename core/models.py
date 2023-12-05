from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
