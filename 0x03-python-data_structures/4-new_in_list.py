#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpd_list = my_list[:]
    if (idx < 0 or idx >= len(my_list)):
        return (cpd_list)
    cpd_list[idx] = element
    return (cpd_list)
