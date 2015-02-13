!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


# def open_zip(datafile):
#     with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#         myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    # get a slice of all values from column 1 - Coast - data
    # Need to slice the data with knowing the number of rows
    number_rows = sheet.nrows

    coast_index = 1

    coast_data = sheet.col_values(coast_index, start_rowx=1, end_rowx=number_rows)
    # print coast_data    

    # calculate the max value based on coast_data column of values
    maxvalue = max(coast_data)

    # calculate min value in coast column
    minvalue = min(coast_data)

    # calculate the average of list values in coast
    # note: use float(len(coast_data)) - can't always guaranatee numerator will be a float
    avgcoast = sum(coast_data)/float(len(coast_data))

    # find the row & col for the time values for min & max entries
    time_index = 0

    # retrieve the format in which the xldate is saved (1900 vs. 1904)
    datemode = workbook.datemode

    # find row number for max value
    for r, value in enumerate(coast_data):
        # tests whether the value is a xldate (the type is value 3)
        if sheet.cell_type(r, time_index) == 3:
            if value == maxvalue:
                # must add 1 to the row index to account for headers
                # in the sheet whereas coast_data list doesn't include headers 
                maxtime = sheet.cell_value(r + 1, time_index)
                maxtime = xlrd.xldate_as_tuple(maxtime, datemode)
                # print maxtime


            if value == minvalue:
                # account for headers, fix the off by one error
                mintime = sheet.cell_value(r + 1, time_index)
                mintime = xlrd.xldate_as_tuple(mintime, datemode)

    data = {
            'maxtime': maxtime,
            'maxvalue': maxvalue,
            'mintime': mintime,
            'minvalue': minvalue,
            'avgcoast': avgcoast
    }

    return data


def test():
    # open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()