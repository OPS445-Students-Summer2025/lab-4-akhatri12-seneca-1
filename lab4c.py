#!/usr/bin/env python3

def create_dictionary(keys, values):
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict

def shared_values(dict1, dict2):
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    return set1 & set2
