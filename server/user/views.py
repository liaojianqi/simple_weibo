from .models import User, Follow
from django.http import JsonResponse, Http404
from common import parameters, auth
from . import utils


TOKEN_LEN = 36


def login(request):
    if request.method == 'GET':
        raise Http404
    try:
        username = parameters.get_parameter_string(request, 'username')
        password = parameters.get_parameter_string(request, 'password')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})
    q = User.objects.filter(username=username)
    if len(q) == 0:
        return JsonResponse({'code': 1, 'msg': 'user not exist'})
    if len(q) != 1:
        return JsonResponse({'code': 1, 'msg': 'database error'})
    for i in q:
        if i.password == password:
            token = utils.token_gen(TOKEN_LEN)
            auth.token_user[token] = i.username
            return JsonResponse({'code': 0, 'data': token})
        else:
            return JsonResponse({'code': 1, 'msg': 'password error'})
    return JsonResponse({'code': 0, 'msg': 'login success'})


def register(request):
    if request.method == 'GET':
        raise Http404

    try:
        username = parameters.get_parameter_string(request, 'username')
        password = parameters.get_parameter_string(request, 'password')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})

    # check if username exist
    q = User.objects.filter(username=username)
    if len(q) != 0:
        return JsonResponse({'code': 1, 'msg': 'user already exist'})

    u = User(username=username, password=password)
    u.save()
    return JsonResponse({'code': 0})


def follow(request):
    if request.method == 'GET':
        raise Http404
    try:
        from_name = parameters.get_parameter_string('username')
        to_name = parameters.get_parameter_string('to_name')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})

    f = Follow(from_name=from_name, to_name=to_name)
    f.save()
    return JsonResponse({'code': 0})


def cancel_follow(request):
    if request.method == 'GET':
        raise Http404
    try:
        from_name = parameters.get_parameter_string('username')
        to_name = parameters.get_parameter_string('to_name')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})
    # delete
    Follow.objects.filter(from_name=from_name, to_name=to_name).delete()
    return JsonResponse({'code': 0})


def follow_list(request):
    if request.method == 'GET':
        raise Http404
    try:
        username = parameters.get_parameter_string(request, 'username')
        offset = parameters.get_parameter_int(request, 'offset')
        limit = parameters.get_parameter_int(request, 'limit')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})

    q = Follow.objects.filter(from_name=username)[offset:limit]
    total = Follow.objects.filter(from_name=username).count()
    follows = []
    for i in q:
        follows.append(i.to_name)

    return JsonResponse({'code': 0, 'data': {
        'follows': follows,
        'offset': offset,
        'limit': limit,
        'total': total,
    }})


def follower_list(request):
    if request.method == 'GET':
        raise Http404
    try:
        username = parameters.get_parameter_string(request, 'username')
        offset = parameters.get_parameter_int(request, 'offset')
        limit = parameters.get_parameter_int(request, 'limit')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})

    q = Follow.objects.filter(to_name=username)[offset:limit]
    total = Follow.objects.filter(to_name=username).count()
    follows = []
    for i in q:
        follows.append(i.to_name)

    return JsonResponse({'code': 0, 'data': {
        'follows': follows,
        'offset': offset,
        'limit': limit,
        'total': total,
    }})
