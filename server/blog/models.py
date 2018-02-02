from django.db import models


class Blog(models.Model):
    author = models.CharField(max_length=255, default='')
    content = models.CharField(max_length=1000, default='')
    created_at = models.DateTimeField()

    def to_json(self):
        return {
            'author': self.author,
            'content': self.content,
            'created_at': self.created_at,
        }
