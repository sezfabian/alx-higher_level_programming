#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        tuple_n = (0, 'none')
        return tuple_n
    else:
        tuple_n = (len(sentence), sentence[0])
        return tuple_n
