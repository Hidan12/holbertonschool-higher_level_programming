#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    tmp_dic = {key: value}
    val = a_dictionary.get(key)
    if (val is not None):
        a_dictionary[key] = value
    else:
        a_dictionary.update(tmp_dic)
    return a_dictionary
