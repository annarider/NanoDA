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
    data = []

    # iterate through each column and compute the requested values
    # must skip first & last columns which contains hour & load to only get stations
    for i in range(1,sheet.ncols - 1):

        # retrieve the name of the station - always row 0 because it's the header 
        station = sheet.cell_value(0, i)
        # take one column (region) from xls in each iteration
        col = sheet.col_values(i, start_rowx=1, end_rowx=None)
        # find the max load in the region
        maxload = max(col)
        # index to find time for corresponding max + 1 to account for headers
        index_time = col.index(maxload) + 1 

        # retrieve the time value from the sheet; time column is first i.e. index=-0.1
        time = sheet.cell_value(index_time, 0)

        # convert the time from xls format to year, month, day, hour

        year, month, day, hour, minute, second = xlrd.xldate_as_tuple(time, workbook.datemode)

        data.append({'Station': station,'Year': year,'Month': month, \
            'Day': day,'Hour': hour,'Max Load': maxload})

    return data

def save_file(data, filename):

    with open(filename, 'wb') as f:
        # set fieldnames
        fn = ['Station','Year','Month','Day','Hour','Max Load']
        # pass in params to writer, incl. header row fieldnames & pipe as delimiter
        writer = csv.DictWriter(f, fieldnames= fn, delimiter="|")
        # write header row
        writer.writeheader()

        # write each row to csv file
        for row in data:
            # must use writerrow for dict, otherwise iterates through keys
            writer.writerow(row)

    
def test():
    # open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

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
