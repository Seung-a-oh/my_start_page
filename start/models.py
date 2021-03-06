from django.db import models

class School(models.Model):
    index = models.CharField(max_length=10)
    title = models.TextField(unique=True)
    link = models.TextField()

    def __str__(self):
        return self.title

class Depart(models.Model):
    index = models.CharField(max_length=10)
    title = models.TextField(unique=True)
    link = models.TextField()

    def __str__(self):
        return self.title

class Memo(models.Model):
    content= models.TextField()

class Go(models.Model):
    name = models.CharField(max_length=20)
    link = models.TextField()