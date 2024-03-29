#!/usr/bin/python3
'''A function that reads a JSON file'''


import json


def save_to_json_file(my_obj, filename):
    '''Saves a doc to a JSON format'''
    with open(filename, 'w+') as f:
        return json.dump(my_obj, f)
