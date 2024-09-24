#!/usr/bin/env python3

class CountedIterator:
    """Iterator class that counts the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0  # Init the counter to track the number of iterations

    def __next__(self):
        """Fetch the next item and increment the counter."""
        try:
            item = next(self.iterator)  # Get the next item from the iterator
            self.count += 1  # Increment the counter
            return item  # Return the next item
        except StopIteration:
            raise StopIteration  # Propagate StopIteration when iteration ends

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return self.count
