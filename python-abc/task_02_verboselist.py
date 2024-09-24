#!/usr/bin/env python3

class VerboseList(list):

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        item_number = len(item)
        super().extend(item)
        print("Extended the list with [{}] items.".format(item_number))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print("Popped [{}] from the list.".format(item))
        else:
            item = super().pop(index)
            print("Popped [{}] from the list.".format(item))
