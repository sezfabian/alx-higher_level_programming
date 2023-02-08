#!/usr/bin/python3
"""7-add_item module"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"


def add_to_json(inpt=sys.argv[1:]):
    """adds input to json file"""
    args = []
    try:
        args = load_from_json_file(filename)
        for i in inpt:
            args.append(i)
    except FileNotFoundError:
        for i in inpt:
            args.append(i)
    save_to_json_file(args, filename)


add_to_json(sys.argv[1:])
