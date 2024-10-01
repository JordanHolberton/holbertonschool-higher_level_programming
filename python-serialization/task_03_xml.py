import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    # Create the root element
    root = ET.Element('data')

    # Iterate over dictionary items and add them as subelements to the root
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    # Write the XML tree to the provided file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from the XML elements
        deserialized_dict = {child.tag: child.text for child in root}

        return deserialized_dict
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None
