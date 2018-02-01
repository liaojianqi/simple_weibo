from django.http import JsonResponse
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
    return JsonResponse({'code': 0})
