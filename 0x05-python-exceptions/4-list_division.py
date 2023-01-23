#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = [0]*list_length
    for i in range(list_length):
        try:
            results[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except (ValueError, TypeError):
            print("wrong type")
        finally:
            continue
    return results
