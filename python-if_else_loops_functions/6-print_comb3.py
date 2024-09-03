#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        # Print the combination of two digits
        print(f"{i}{j}", end="")
        # Add a comma and space after every combination except the last one
        if i != 8 or j != 9:
            print(", ", end="")
print()
