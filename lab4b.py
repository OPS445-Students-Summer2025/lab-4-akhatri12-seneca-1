#!/usr/bin/env python3

def join_lists(l1, l2):
    return list(set(l1).union(set(l2)))

def match_lists(l1, l2):
    return list(set(l1).intersection(set(l2)))

def diff_lists(l1, l2):
    return list(set(l1).symmetric_difference(set(l2)))
