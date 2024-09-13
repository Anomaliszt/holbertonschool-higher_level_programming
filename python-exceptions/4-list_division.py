#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = [0] * list_length

    for i in range(list_length):
        try:
            results[i] = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            results[i] = 0
        except TypeError:
            print("wrong type")
            results[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            results[i] = 0
        finally:
            pass
    return results
