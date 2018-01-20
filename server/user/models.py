from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')

    # 不能重写构造方法
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
