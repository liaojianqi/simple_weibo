import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import auth


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/user/login' \
                or request.path == '/user/register':
            return self.get_response(request)

        username = auth.auth(request)
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['username'] = username
        return self.get_response(request)
