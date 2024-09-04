#!/usr/bin/python3
from add_0 import add  # Correctly import the 'add' function

a = 1  # Assign value 1 to variable a
b = 2  # Assign value 2 to variable b

# Print the result of the addition in the required format
print("{} + {} = {}".format(a, b, add(a, b)))
