#!/usr/bin/env python3
import pickle

class CustomObject:
    """Add class represent name, age and is_student"""

    def __init__(self, name, age, is_student):
        """initialize a new CustomObject instance

        Args:
            name (str): name of the object
            age (int): age of the object
            is_student (boolean): if the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self)
        """Print all arguments in readable format"""
        print(f."Name: {self.name}")
        print(f."Age: {self.age}")
        print(f."Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object and save it to a file.

        Args:
            filename (str): The file to which the object should be serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}.")
        except Exception as e:
            print(f"Failed to serialize object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file and return the instance.

        Args:
            filename (str): The file from which to deserialize the object.

        Returns:
            CustomObject or None: The deserialized object, or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Failed to deserialize object: {e}")
            return None