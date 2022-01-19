#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    b = 0
    resul = 0
    result = []
    tam = list_length
    try:
        for a in range(tam):
            try:
                resul = my_list_1[a] / my_list_2[a]
                result.append(resul)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except (ValueError, TypeError):
                print("wrong type")
                result.append(0)
    except IndexError:
        print("out of range")
        result.append(0)
    return(result)
