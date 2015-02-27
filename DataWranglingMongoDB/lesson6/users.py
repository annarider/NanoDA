#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    # retrieve the dictionary with all items in the element
    element_dict = element.attrib
    # only proceed if 'user' is a valid attribute in the element
    if 'user' in element_dict:
        # find the value of 'user' in the node element
        user = element_dict['user']
        return user
    else:
        # didn't find 'user' so return None
        return None

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        user = get_user(element)
        # if valid user, add to set (set will only add unique users)
        if user != None:
            users.add(user)
    return users


def test():

    users = process_map('example2.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()