import random
import string


# token generation
def token_gen(n):
    return ''.join(random.choices(string.digits + string.ascii_letters, k=n))


def auth(request):
    token = request.META.get('token')
    if token is None:
        raise ValueError('')