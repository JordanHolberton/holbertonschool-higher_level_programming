#!/usr/bin/python3
"""Function for return the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """return the JSON representation of an object"""
    return json.dumps(my_obj)
