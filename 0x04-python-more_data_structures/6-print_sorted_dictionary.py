#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = a_dictionary.keys()
    key = sorted(key)
    tmp_dic = {}
    dic = {}
# esta parte de codigo sirve para añadir nuevo diccionario
    for a in key:
        tmp_dic = {a: a_dictionary[a]}
        dic.update(tmp_dic)
    for b in key:
        print("{}: {}".format(b, dic[b]))
