from django.db import models


class Blog(models.Model):
    author = models.CharField(max_length=255, default='')
    content = models.CharField(max_length=1000, default='')
