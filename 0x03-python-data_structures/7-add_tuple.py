#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a and not tuple_b:
        tuple_x = (0, 0)
        return tuple_x
    elif not tuple_a:
        return tuple_b
    elif not tuple_b:
        return tuple_a
    else:
        new = [0, 0]
        if len(tuple_a) < 2 and len(tuple_b) < 2:
            new[0] = tuple_a[0] + tuple_b[0]
        elif len(tuple_a) < 2:
            new[0] = tuple_a[0] + tuple_b[0]
            new[1] = tuple_b[1]
        elif len(tuple_b) < 2:
            new[0] = tuple_a[0] + tuple_b[0]
            new[1] = tuple_a[1]
        else:
            new[0] = tuple_a[0] + tuple_b[0]
            new[1] = tuple_a[1] + tuple_b[1]
        tuple_n = (new[0], new[1])
        return tuple_n
