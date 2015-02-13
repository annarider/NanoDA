# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    # init list variable to store all the dicts
    data = []
    # count number of rows to ensure only process 10 rows
    row_count = 0
    
    # list to store header row
    header = []

    with open(datafile, "r") as f:
        for line in f:

            # processes line to remove whitespaces & stores values as rows in list
            row = line.strip().split(',')
            
            # save the header to call as keys for dict later
            if row_count == 0:
                header = row

            # doesn't process row 1 which is the header and stops after first 10 data lines 
            if row_count != 0 and row_count <= 10:
            
            # init variable i to index through rows in data list 
                i = 0 
                # dict to store the data in one line
                data_1line = {}             
                for element in row:

                    # create key & set value to be element (i.e. value) for current row
                    data_1line[header[i]] = element
                    # increment index by 1
                    i += 1

                # add dict to data list
                data.append(data_1line)

            # break out of for loop after saving first 10 lines
            if row_count > 10:
                break
            row_count += 1

    # return 10 dicts in list, each dict representing one row
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    # print "d =" 
    # print d
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()