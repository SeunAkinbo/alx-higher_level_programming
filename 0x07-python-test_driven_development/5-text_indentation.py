#!/usr/bin/python3

'''The module contains a function that prints a text with
2 newlines after each of these characters . , ? and :
Module: 5-text_indentation
Function: text_indentation
'''


def text_indentation(text):
    '''
    prints a text with2 newlines after each of these characters . , ? and :
    Parameter: text (string)
    '''

    '''Validates text'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    '''Execute operation'''
    new_text = ""
    for char in text:
        new_text += char
        if char in ".?:":
            print(new_text.strip())
            print()
            new_text = ""

    if new_text:
        print(new_text.strip())
