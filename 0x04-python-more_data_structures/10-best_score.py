#!/usr/bin/python3
def best_score(a_dictionary):
    name = None
    score = 0
    if (a_dictionary is not None):
        for a in a_dictionary:
            if (score < a_dictionary[a]):
                name = a
                score = a_dictionary[a]
        return name
    else:
        return None
