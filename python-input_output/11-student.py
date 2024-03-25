#!/usr/bin/python3
'''Class that defines a student'''


class Student:
    '''Student class'''
    
    def __init__(self, first_name, last_name, age):
        '''Initializes the student data shaa'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns a dictionary representation of the data'''
        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        if attrs is None or not isinstance(attrs, list):
            return context
        else:
            cont = {}
            for item in attrs:
                if not isinstance(item, str):
                    return context
                if item in context:
                    cont[item] = context[item]
            return cont

    def reload_from_json(self, json):
        '''Reloads object attributes from a JSON dictionary'''
        for key, value in json.items():
            setattr(self, key, value)
