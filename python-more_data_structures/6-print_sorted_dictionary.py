#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for orderkey in sorted(a_dictionary):
        print("{}: {}".format(orderkey, a_dictionary[orderkey]))
