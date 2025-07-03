#!/usr/bin/env python3

def join_sets(s1, s2):
    return s1 | s2

def match_sets(s1, s2):
    return s1 & s2

def diff_sets(s1, s2):
    return s1 ^ s2
