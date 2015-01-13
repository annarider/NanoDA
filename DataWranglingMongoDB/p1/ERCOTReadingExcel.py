#!/usr/bin/env python
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

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    
    # get the data from xls, put it in rows & cols for retrieval
    sheet_data = [[sheet.cell_value(r, col) 
                        for col in range(sheet.ncols)] 
                            for r in range(sheet.nrows)]

    # get a slice of all values from column 1 - Coast - data
    # Need to slice the data with knowing the number of rows
    number_rows = sheet.nrows

    coast_index = 1

    coast_data = sheet.col_values(coast_index, start_rowx=1, end_rowx=number_rows)
    # print coast_data
    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }

    # calculate the max value based on coast_data column of values
    maxvalue = max(coast_data)
    data['maxvalue'] = maxvalue
    # calculate 

    # calculate min value in coast column
    minvalue = min(coast_data)
    data['minvalue'] = minvalue

    avgcoast = sum(coast_data)/number_rows
    data['avgcoast'] = avgcoast

    # find the row & col for the time values for min & max entries
    time_index = 0
    # find row number for max value
    for r, value in enumerate(coast_data):
        if value == maxvalue:
            maxtime = sheet_data[r][time_index]
            maxtime = xlrd.xldate_as_tuple(maxtime, 0)
            print maxtime
            data['maxtime'] = maxtime
            break




    return data


def test():
    # open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()