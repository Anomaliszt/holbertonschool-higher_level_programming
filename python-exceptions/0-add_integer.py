#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for element in my_list:
        if count >= x:
            break
        try:
            print(element, end="")
            count += 1
        except Exception:
            break
    print()
    return count
