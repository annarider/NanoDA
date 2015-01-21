"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'


'''
Pseudo-code
All tests that need to be done to check for validity: 
1. Check if productionStartYear is not NULL
2. If not null, remove the first 4 characters 
(all datetime format is year, month, day sequence)
3. Check if the year is between 1886-2014
4. Check the URI starts contains substring 'http://dbpedia.org'
If it passes all these tests: then save in index of line in a valid_years
If it doesn't pass the test, then save indx of line in invalid_years
Write all valid lines to output_good and all invalid lines to output_bad
'''

# This function performs the tests outlined about, calling helper functions
# when needed
def check_valid_year(reader):
    valid_years = []
    invalid_years = []
    check_dbpedia_string = 'http://dbpedia.org'

    for i, row in enumerate(reader): 
        # test if year equals string 'NULL'
        if row['productionStartYear'] != 'NULL':
            datetime = row['productionStartYear']

            # test if first 4 digits are a valid 
            year = datetime[0:4]

            ''' check if the 4 characters in string format can be 
            represented as a number '''
            def is_number(s):
                try: 
                    int(s)
                    return True
                except ValueError:
                    return False

            if year != None:
                check_year_is_number = is_number(year)
                # proceed with tests if year is a number, otherwise line is invalid
                if check_year_is_number == True:
                    # requires testing for length = 4 & if year falls between 1886-2014 
                    if len(year) == 4 and int(year) >= 1886 and int(year) <= 2014:
                # check if URI contains DBpedia domain
                        uri = row['URI']
                        if 'http://dbpedia.org' in uri:
                            valid_years.append(i)
        else:
            invalid_years.append(i)

    return valid_years, invalid_years    

'''
Takes the valid_years list and writes out all the lines with valid years
'''

def write_output_good(output_good, reader, header, valid_years):

    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        print 'reference at= ', reader
        for i, row in enumerate(reader):
            print row
            if i in valid_years:
                writer.writerow(row)
                print 'yes'


def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        print 'reference at= ', reader
        # why does this row print? ...
        # comment out this for loop and see the two valid & invalid year lists 
        # print with values inside lists
        for row in reader:
            print row

        valid_years, invalid_years = check_valid_year(reader)
        print 'valid_years= ', valid_years
        print 'invalid_years= ', invalid_years
        # ... but this row will not print after i have passed around the reader object?
        for row in reader:
            print row

        write_output_good(output_good, reader, header, valid_years)

        # again, reader object exists but why can't I print out any rows?
        print 'reference at= ', reader

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()