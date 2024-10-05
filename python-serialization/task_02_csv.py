#!/usr/bin/python3
"""CSV file to Python"""


def convert_csv_to_json(csv_file):
    """ The Function """
    import csv
    import json

    data = []
    try:
        with open(csv_file, "r") as file:
            read = csv.DictReader(file)
            for row in read:
                data.append(row)
    except FileNotFoundError:
        print("file not found")
        return False

    with open("data.json", "w") as file:
        file.write(json.dumps(data))
    return True
