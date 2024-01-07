#!/usr/bin/python3

def no_c(my_string):
    new = my_string
    for i in range(len(new)):
        if new[i] == c or new[i] == C:
            new[i] = ""
    return(new)
