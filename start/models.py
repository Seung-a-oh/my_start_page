from django.db import models

class School(models.Model):
    index = models.CharField(max_length=10,unique=True)
    title = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.index

