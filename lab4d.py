#!/usr/bin/env python3

def first_five(s):
    return s[:5]

def last_seven(s):
    return s[-7:]

def middle_number(num):
    s = str(num)
    return s[1:3]

def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]
