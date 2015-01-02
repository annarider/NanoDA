import sys
import string
import logging
import csv

# from util import mapper_logfile
# logging.basicConfig(filename=mapper_logfile, format='%(message)s',
#                     level=logging.INFO, filemode='w')

def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")

    
    with open('aadhaar_data.csv', 'rb') as file:
        reader = csv.reader(file)
        
        count_row = 0 

        # district is the fourth column in the csv file, hard coded here
        district = 3
        # aadhaar generated is 9th column in csv file
        aadhaar_generated = 8

        for line in reader:
            if count_row != 0:

                # tokenize each line by the commas
                # data = line.strip.split(",")
                if len(line) == 12:

                    print "{0}\t{1}".format(line[district], line[aadhaar_generated])

            count_row += 1 
    # for line in sys.stdin:
        
            

        
            # print data 

mapper()
