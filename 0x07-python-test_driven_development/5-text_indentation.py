#!/usr/bin/python3
def text_indentation(text):
    """indentation"""
    tmp = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for a in range(len(text)):

            if (text[a] != '.' and text[a] != "?" and text[a] and ":" and not tmp):
                print("{}".format(text[a]), end="")
            elif text[a + 1] == " ":
                print("{}".format(text[a]), end="")
                tmp = True
            try:
                if  text[a + 1] != " " and tmp:
                    print("")
                    print("")
                    tmp = False
            except IndexError:
                pass
