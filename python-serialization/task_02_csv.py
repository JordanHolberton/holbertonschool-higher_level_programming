import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON and save it as data.json.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read data
        with open(csv_filename, mode='r', newline='') as csv_file:
            # Use DictReader to convert each row into a dictionary
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON and write to data.json
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
