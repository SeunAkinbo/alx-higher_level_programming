#!/usr/bin/python3
def multiple_returns(sentence):
    char = sentence[0] if sentence[0] != '' else None
    return (len(sentence), char)
