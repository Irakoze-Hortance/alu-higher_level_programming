#!/usr/bin/python3
'''Appends a string at the end of a text file (UTF8)'''


def append_write(filename="", text=""):
    '''Function to write text to a file'''
    with open(filename, 'a+') as f:
        return f.write(text)
