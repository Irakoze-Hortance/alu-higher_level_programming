#!/usr/bin/python3
'''A function that returns the available attributes and methods of an object'''


def lookup(obj):
    '''Take an object and return its attributes and methods'''
    return list(dir(obj))
