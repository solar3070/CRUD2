from django.db import models

class Album(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
