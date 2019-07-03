from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
