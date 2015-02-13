#-*- coding: UTF-8 -*-
def _(value):
    return value


def make_GET_url(url, query_dict):
    # generate a GET url
    # TODO: change to python urllib
    if not isinstance(query_dict, dict):
        raise AttributeError()
    tmp = ""
    for key in query_dict:
        tmp += "%s=%s&" % (key, query_dict[key])

    return "%s?%s" % (url, tmp[:-1])



def model_choice_2_dict(choice_obj):
    if not isinstance(choice_obj, tuple):
        raise AttributeError()

    result_dict = {}
    for element in choice_obj:
        result_dict[element[0]] = element[1]

    return result_dict


def handle_upload_file(f, saved_name, path):
    with open(path + saved_name, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)