from .models import User, Follow
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
    return JsonResponse({'code': 0})


def follow(request):
    if request.method == 'GET':
        raise Http404

    from_name = request.POST.get('from_name')
    if from_name is None:
        return JsonResponse({'code': 1, 'msg': 'parameter from_name must be provide'})

    to_name = request.POST.get('to_name')
    if to_name is None:
        return JsonResponse({'code': 1, 'msg': 'parameter to_name must be provide'})

    f = Follow(from_name=from_name, to_name=to_name)
    f.save()
    return JsonResponse({'code': 0})


def cancel_follow(request):
    if request.method == 'GET':
        raise Http404

    from_name = request.POST.get('from_name')
    if from_name is None:
        return JsonResponse({'code': 1, 'msg': 'parameter from_name must be provide'})

    to_name = request.POST.get('to_name')
    if to_name is None:
        return JsonResponse({'code': 1, 'msg': 'parameter to_name must be provide'})

    # delete
    Follow.objects.filter(from_name=from_name, to_name=to_name).delete()
    return JsonResponse({'code': 0})


def follow_list(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if username is None:
            return JsonResponse({'code': 1, 'msg': 'parameter username must be provide'})
        cnt = Follow.objects.filter(from_name=username).count()

        return JsonResponse({'code': 0, 'data': cnt})

    username = request.POST.get('username')
    if username is None:
        return JsonResponse({'code': 1, 'msg': 'parameter username must be provide'})

    offset_s = request.POST.get('offset')
    if offset_s is None:
        return JsonResponse({'code': 1, 'msg': 'parameter offset must be provide'})
    try:
        offset = int(offset_s)
    except ValueError as e:
        return JsonResponse({'code': 1, 'msg': e.__str__()})

    limit_s = request.POST.get('limit')
    if limit_s is None:
        return JsonResponse({'code': 1, 'msg': 'parameter limit must be provide'})
    try:
        limit = int(limit_s)
    except ValueError as e:
        return JsonResponse({'code': 1, 'msg': e.__str__()})

    q = Follow.objects.filter(from_name=username)[offset:limit]
    l = []
    for i in q:
        l.append(i.to_name)

    return JsonResponse({'code': 0, 'data': l})


def follower_list(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if username is None:
            return JsonResponse({'code': 1, 'msg': 'parameter username must be provide'})
        cnt = Follow.objects.filter(to_name=username).count()

        return JsonResponse({'code': 0, 'data': cnt})

    username = request.POST.get('username')
    if username is None:
        return JsonResponse({'code': 1, 'msg': 'parameter username must be provide'})

    offset_s = request.POST.get('offset')
    if offset_s is None:
        return JsonResponse({'code': 1, 'msg': 'parameter offset must be provide'})
    try:
        offset = int(offset_s)
    except ValueError as e:
        return JsonResponse({'code': 1, 'msg': e.__str__()})

    limit_s = request.POST.get('limit')
    if limit_s is None:
        return JsonResponse({'code': 1, 'msg': 'parameter limit must be provide'})
    try:
        limit = int(limit_s)
    except ValueError as e:
        return JsonResponse({'code': 1, 'msg': e.__str__()})

    q = Follow.objects.filter(to_name=username)[offset:limit]
    l = []
    for i in q:
        l.append(i.from_name)

    return JsonResponse({'code': 0, 'data': l})
