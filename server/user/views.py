from .models import User
from django.http import HttpResponse


def login(request):
    username = 'loin1'
    q = User.objects.filter(username=username)
    if len(q) == 0:
        return HttpResponse("user not exist")
    return HttpResponse("login success")

