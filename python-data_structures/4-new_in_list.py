#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
