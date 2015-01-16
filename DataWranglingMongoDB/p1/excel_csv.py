# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


# def open_zip(datafile):
#     with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#         myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = None

    # iterate through each column and compute the requested values
    for i in range(sheet.ncols):

        # retrieve the name of the station - always row 0 because it's the header 
        station = sheet.cell_value(0, i)
        # take one column (region) from xls in each iteration
        col = sheet.col_values(i, start_rowx=1, end_rowx=None)
        # find the max load in the region
        maxload = max(col)
        # index to find time for corresponding max + 1 to account for headers
        index_time = index(maxload) + 1 

        time = col[index_time]

        # convert the time from xls format to year, month, day, hour

        year, month, day, hour = xlrd.xldate_as_tuple(time, workbook.datemode)

        data.append([]) 



    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    return data

def save_file(data, filename):
    # YOUR CODE HERE
    pass
    
def test():
    # open_zip(datafile)
    data = parse_file(datafile)
    # save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()
