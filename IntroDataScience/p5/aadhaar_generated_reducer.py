import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
        
    aadhaar_generated = {}

    for line in sys.stdin:
        data = line.strip().split("\t")

        key, aadhaar_count = data
        aadhaar_count = int(aadhaar_count)

        if key in aadhaar_generated: 
            aadhaar_generated[key] += aadhaar_count
        else: 
            aadhaar_generated[key] = aadhaar_count

    for key in aadhaar_generated:
        print "{0}\t{1}".format(key, aadhaar_generated[key])
    

    old_key = None
    key_history = []

    for line in sys.stdin:
        # data = line.strip.split("\t")

        if len(data) == 2:
            this_key, aadhaar_count = data

            if old_key and old_key != this_key:
                print "{0}\t{1}".format(old_key, aadhaar_count)
                aadhaar_count = 0

            old_key = this_key
            aadhaar_count += 1

        if old_key != None:
            print "{0}\t{1}".format(old_key, aadhaar_count)

reducer()
