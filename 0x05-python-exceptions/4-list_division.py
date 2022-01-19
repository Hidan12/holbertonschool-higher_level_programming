#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    b = 0
    resul = 0
    result = []
    tam = list_length
    for a in range(tam):
        try:
            resul = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
            resul = 0
        except (ValueError, TypeError):
            print("wrong type")
            resul = 0
        except IndexError:
            print("out of range")
            resul = 0
        finally:
            result.append(resul)
    return(result)
