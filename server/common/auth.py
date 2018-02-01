from django.core.exceptions import PermissionDenied

COOKIE_SALT = 'bvw289v1nerw3vjuaqe'
# token -> username
token_user = {}


def auth(request):
    token = request.META.get('HTTP_TOKEN')
    if token is None:
        raise PermissionDenied('token must be provide.')
    username = token_user.get(token)
    if username is None:
        raise PermissionDenied('token is invalid.')
    return username
