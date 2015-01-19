#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
# This is example of the datastructure you should return
# Each item in the list should be a dictionary containing all the relevant data
# Note - year, month, and the flight data should be integers
# You should skip the rows that contain the TOTAL data for a year
# data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#         },
#         {"courier": "..."}
# ]
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
import re

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    # This is example of the datastructure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    data = []

    
    with open("{}/{}".format(datadir, f), "r") as html:
    # with open(f, "r") as html:

        soup = BeautifulSoup(html)
        # extract all table row elements with class = dataTDRight
        table = soup.find_all('tr', {'class': 'dataTDRight'})
        
        for row in table:
            # extract_data = {"courier": info['courier'], "airport": info['airport']}
            extract_data = []
            # init constants to iterate through extract data list   
            YEAR = 0
            MONTH = 1
            DOMESTIC = 2
            INTERNATIONAL = 3
            for value in row.find_all('td'):
                # add all values to extract data list to process later
                extract_data.append(value.get_text().strip())
            if extract_data[MONTH] != 'TOTAL':
                info = {}
                info["courier"], info["airport"] = f[:6].split("-")
                info['year'] = int(extract_data[YEAR])
                info['month'] = int(extract_data[MONTH])
                dom_val = re.sub('[\W_]', "", extract_data[DOMESTIC])
                intl_val = re.sub('[\W_]', "", extract_data[INTERNATIONAL])
                info['flights'] = {'domestic': int(dom_val), 'international': int(intl_val)}
                data.append(info)
  

        print data

    return data


def test():
    print "Running a simple test..."
    open_zip(datadir)
    files = process_all(datadir)
    data = []
    for f in files:
        data += process_file(f)
    assert len(data) == 399
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
    print "... success!"

if __name__ == "__main__":
    test()