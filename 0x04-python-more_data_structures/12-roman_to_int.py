#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for j in roman_string:
        if (d.get(j) is None):
            return 0
    for i in range(len(roman_string)):
        if (len(roman_string) == 1 or (len(roman_string) - 1) == i):
            sum += d[roman_string[i]]
        elif((d[roman_string[i]] < d[roman_string[i + 1]])):
            sum += (d[roman_string[i + 1]] - d[roman_string[i]])
            i += 1
            if(len(roman_string) == i + 1):
                break
        else:
            sum += (d[roman_string[i]])
    return(sum)
