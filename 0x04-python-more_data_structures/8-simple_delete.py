#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    val = a_dictionary.get(key)
    if (val is not None):
        a_dictionary.pop(key)
