from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from common import parameters
from .models import Blog


def create_blog(request):
    try:
        username = parameters.get_parameter_string(request, 'username')
        content = parameters.get_parameter_string(request, 'content')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})
    blog = Blog(author=username, content=content)
    blog.save()
    return JsonResponse({'code': 0, 'data': blog.id})


def delete_blog(request):
    try:
        username = parameters.get_parameter_string(request, 'username')
        _id = parameters.get_parameter_int(request, 'id')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})
    # validate
    q = Blog.objects.filter(id=_id)
    if len(q) != 1:
        return JsonResponse({'code': 1, 'msg': 'id is invalid!'})
    for i in q:
        if i.author != username:
            raise PermissionDenied('user valid')
    Blog.objects.filter(id=_id).delete()
    return JsonResponse({'code': 0})


# list user all blog
def list_blog(request):
    try:
        username = parameters.get_parameter_string(request, 'username')
        offset = parameters.get_parameter_int(request, 'offset')
        limit = parameters.get_parameter_int(request, 'limit')
    except Exception as e:
        return JsonResponse({'code': 1, 'msg': str(e)})

    blogs = Blog.objects.filter(author=username).order_by('-created_at')[offset:limit]
    total = Blog.objects.filter(author=username).count()
    return JsonResponse({'code': 0, 'data': {
        'blogs': [o.to_json() for o in blogs],
        'offset': offset,
        'limit': limit,
        'total': total,
    }})
