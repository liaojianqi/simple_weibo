from .models import User
from django.http import JsonResponse, Http404


def login(request):
    if request.method == 'GET':
        raise Http404

    username = request.POST.get('username')
    if username is None:
        return JsonResponse({'code': 1, 'msg': 'parameter username must be provide'})

    password = request.POST.get('password')
    if password is None:
        return JsonResponse({'code': 1, 'msg': 'parameter password must be provide'})

    q = User.objects.filter(username=username)
    if len(q) == 0:
        return JsonResponse({'code': 1, 'msg': 'user not exist'})

    if len(q) != 1:
        return JsonResponse({'code': 1, 'msg': 'database error'})

    for i in q:
        if i.password == password:
            return JsonResponse({'code': 0, 'msg': 'login success'})
        else:
            return JsonResponse({'code': 1, 'msg': 'password error'})

    return JsonResponse({'code': 0, 'msg': 'login success'})


def register(request):
    if request.method == 'GET':
        raise Http404

    username = request.POST.get('username')
    if username is None:
        return JsonResponse({'code': 1, 'msg': 'parameter username must be provide'})

    password = request.POST.get('password')
    if password is None:
        return JsonResponse({'code': 1, 'msg': 'parameter password must be provide'})

    # check if username exist
    q = User.objects.filter(username=username)
    if len(q) != 0:
        return JsonResponse({'code': 1, 'msg': 'user already exist'})

    u = User(username=username, password=password)
    u.save()
    return JsonResponse({'code': 0, 'msg': 'register success'})
