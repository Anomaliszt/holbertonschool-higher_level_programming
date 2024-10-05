#!/usr/bin/python3
""" basic serialization module that adds
the functionality to serialize a Python dictionary to a
JSON file and deserialize the JSON file
to recreate the Python Dictionary
"""


def serialize_and_save_to_file(data, filename):
    """Serialize to JSON """
    import json
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """deserialize from JSON."""
    import json
    with open(filename, "r") as file:
        data = json.load(file)
    return data
