#!/usr/bin/python3
"""Module documentation.

This module contains a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)