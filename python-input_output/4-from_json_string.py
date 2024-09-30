#!/usr/bin/python3
"""Defines a file-writing function"""
import json


def from_json_string(my_str):
    return json.load(my_str)