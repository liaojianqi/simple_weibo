import random
import string


# token generation
def token_gen(n):
    return ''.join(random.choices(string.digits + string.ascii_letters, k=n))
