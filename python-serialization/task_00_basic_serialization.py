import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file to save the data to.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file into a Python dictionary.

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        dict: The deserialized Python dictionary from the JSON file.
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
