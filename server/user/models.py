from django.db import models
from json import JSONDecoder, JSONEncoder


class User(models.Model):
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')

    # 不能重写构造方法
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password


class Follow(models.Model, JSONDecoder, JSONEncoder):
    from_name = models.CharField(max_length=255, default='')
    to_name = models.CharField(max_length=255, default='')

