#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dic = {}
    dic = {}
    for a in a_dictionary:
        tmp_dic = {a: (a_dictionary[a] * 2)}
        dic.update(tmp_dic)
    return dic
