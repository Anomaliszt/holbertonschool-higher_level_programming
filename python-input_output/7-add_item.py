#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_obj = []

if os.path.exists(filename):
    my_obj = load_from_json_file(filename)

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        my_obj.append(i)

save_to_json_file(my_obj, filename)
