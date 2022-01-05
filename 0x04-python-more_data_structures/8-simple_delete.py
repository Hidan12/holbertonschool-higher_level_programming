#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    val = a_dictionary.get(key)
    if (val is not None):
        del a_dictionary[key]
    return a_dictionary
