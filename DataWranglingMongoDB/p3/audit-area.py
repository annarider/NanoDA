#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint
import re

CITIES = 'cities.csv'


def fix_area(area):
    # placeholder to be converted to a float later
    area_to_convert = area
    # check if the area string has a '{' and is therefore an array
    if '{' in area:
        # remove the {} and check which value has more significant digits
        stripped_area = re.sub('[{}]', '', area)
        area_list = stripped_area.split('|')
        # since there is an array, test to see which has more significant
        # digits, pick the area with the longest length & assign back to area
        if len(area_list[0]) >= len(area_list[1]):
            area_to_convert = area_list[0]
        else: 
            area_to_convert = area_list[1]

    # convert the area value into a float
    area = convert_to_float(area_to_convert)

    return area

'''
Method to convert area string to a float. If can't be converted, 
then return None
'''
def convert_to_float(s):
    try:
        # if string can be converted to a float, then return the float
        float_area = float(s.strip())
        return float_area
    except ValueError:
        return None


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[8]["areaLand"] == 55166700.0
    assert data[3]["areaLand"] == None


if __name__ == "__main__":
    test()