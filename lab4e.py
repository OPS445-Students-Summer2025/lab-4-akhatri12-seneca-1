#!/usr/bin/env python3

def is_digits(sobj):
    for char in sobj:
        if char not in '0123456789':
            return False
    return True
