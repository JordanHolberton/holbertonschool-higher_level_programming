#!/usr/bin/python3
"""Defines a file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)
