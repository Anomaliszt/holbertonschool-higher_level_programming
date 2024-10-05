#!/usr/bin/python3
""" serialization and deserialization using XML
as an alternative format to JSON
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ serialize to XML """
    root = ET.Element('data')
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """deserialize from xml """
    tree = ET.parse(filename)
    root = tree.getroot()
    dict = {}
    for child in root:
        dict[child.tag] = child.text
    return dict
