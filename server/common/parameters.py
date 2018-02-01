def get_parameter_string(request, key):
    value = request.POST.get(key)
    if value is None:
        raise ValueError('parameter {} must be provide.'.format(key))
    return value


def get_parameter_int(request, key):
    value_s = request.POST.get(key)
    if value_s is None:
        raise ValueError('parameter {} must be provide.'.format(key))
    value_i = int(value_s)
    return value_i


def get_parameter_from_header(request, key):
    value = request.META.get(key)
    if value is None:
        raise ValueError('parameter {} must be provide.'.format(key))
    return value
