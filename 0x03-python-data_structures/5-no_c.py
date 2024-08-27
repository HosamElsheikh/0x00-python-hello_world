#!/usr/bin/python3
def no_c(my_string):
    cpd_string = ""
    for i in range(len(my_string)):
        if (ord(my_string[i]) == ord('c') or ord('C') == ord(my_string[i])):
            continue
        cpd_string += my_string[i]
    return (cpd_string)
