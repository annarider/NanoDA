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
    # init dictionary fieldtypes with keys from the fields list
    # and values are empty sets to be filed with data types later
    fieldtypes = dict([ (field,set()) for field in fields])

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        # skip first 3 lines because header & 2 metadata lines
        for i in range(3):
            reader.next()

        # iterate through every row
        for row in reader:
            # select specific columns to test the data type
            for field in fields:
                val = row[field]
                # GREAT debugging tip!! datatype = return_datatype(val, field=='areaLand')
                datatype = return_datatype(val, field=='areaLand')
                # add datatype to set for the particular fieldname
                fieldtypes[field].add(datatype)


    return fieldtypes

'''
Test the data types and return the type of data
'''
def return_datatype(val, verbose):
                
    # if field has value 'NULL' or empty string, add to NoneType
    if val == 'NULL' or val == '':
        return type(None)
    # if field has value that starts with '{', add to list
    if '{' in val:
        return type([])
    if check_valid_int(val):
        return type(1)
    if check_valid_float(val):
        return type(1.1)
    else:
        if verbose:
            print val
        return type('this problem sucks')
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
        float(s.strip())
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
