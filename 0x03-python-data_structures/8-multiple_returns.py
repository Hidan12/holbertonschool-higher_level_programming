#!/usr/bin/python3
def multiple_returns(sentence):
    tam = len(sentence)
    if sentence == "":
        return(tam, None)
    else:
        return(tam, sentence[0])
