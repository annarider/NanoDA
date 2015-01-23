#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some 
particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.
ou 
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = { 'NoneType': 0, 'list': 0, 'int': 0, 'float': 0, 'str':0 }

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        # iterate through every row
        for row in reader:
            # select specific columns to test the data type
            for field in FIELDS:
                # start testing the data types
                # if field has value 'NULL' or empty string, add to NoneType
                if row[field] == 'NULL' or row[field] == '':
                    fieldtypes['NoneType'] += 1
                # if field has value that starts with '{', add to list
                if '{' in row[field]:
                    fieldtypes['list'] += 1
                if check_valid_int(row[field]):
                    fieldtypes['int']
                if not check_valid_int and check_valid_float:
                    fieldtypes['float']
                else:
                    fieldtypes['str'] += 1

    return fieldtypes

'''
Check if the number is a valid int
'''
def check_valid_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

'''
Check if the number is a valid float
'''
def check_valid_float(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
