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

INPUT_FILE = 'autos-shortened.csv'
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
def check_valid_year(row):
    check_dbpedia_string = 'http://dbpedia.org'
    # begin checks
    if row['productionStartYear'] != 'NULL':
        datetime = row['productionStartYear']

        # test if first 4 digits are a valid 
        year = extract_year(datetime)

        # once year is extracted, continue with tests to check if year is
        # an int and fall within the approved range
        if year != None:
            check_year_is_number = is_number(year)
            # proceed with tests if year is a number, otherwise line is invalid
            if check_year_is_number == True:
                # requires testing for length = 4 & if year falls between 1886-2014 
                if len(year) == 4 and int(year) >= 1886 and int(year) <= 2014:
                    return True
    else:
        return False

'''
Check if URI contains DBpedia domain                    
If URI is from dbpedia, return True, else False
'''
def check_valid_domain(row):
    uri = row['URI']
    if 'http://dbpedia.org' in uri:
        return True
    else: 
        return False

''' 
Check if the 4 characters in string format can be 
represented as a number 
'''
def is_number(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

''' 
Extract the first four characters from datetime but does not check if
it is a valid number - so it could be a string of http
'''
def extract_year(datetime):
    year = datetime[0:4]
    return year

'''
Takes the valid_years list and writes out all the lines with valid years
'''

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f,\
         open(output_good, "w") as g, open(output_bad, "w") as h:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        # create writer for output good file
        # and set the header row in output_good file
        writer_output_good = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer_output_good.writeheader()
        
        # create writer for output good file
        # set the header row in output_good file
        writer_output_bad = csv.DictWriter(h, delimiter=",", fieldnames= header)
        writer_output_bad.writeheader()
        
        for i, row in enumerate(reader):
            if check_valid_domain(row): 
                if check_valid_year(row):
 
                    # productionStartYear transform from datetime to year 
                    row['productionStartYear'] = extract_year(row['productionStartYear'])
                    writer_output_good.writerow(row)
                else:
                    writer_output_bad.writerow(row)
 
            
        
def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()