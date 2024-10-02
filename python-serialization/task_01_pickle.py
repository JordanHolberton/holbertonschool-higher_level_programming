import pickle


class CustomObject:
    """custom object with attributes name, age, and is_student."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object and save it to a file.

        Args:
            filename (str): The file to which the object should be serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file and return the instance.

        Args:
            filename (str): The file from which to deserialize the object.

        Returns:
            CustomObject or None
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Failed to deserialize object: {e}")
            return None
