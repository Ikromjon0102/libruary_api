from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=200)
    sub_name = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=30, decimal_places=2)


    def __str__(self):
        return self.title