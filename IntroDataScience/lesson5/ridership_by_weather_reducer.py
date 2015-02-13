import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable 
    riders and num_hours below. Feel free to use a different data structure in 
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    '''

    ridership = {}
    num_hours = 0   # The number of hours with this key


    for line in sys.stdin:
        
        data = line.strip().split("\t")
        
        weather, entries = data
        entries = float(entries)

        if weather in ridership:
            entries = ridership[weather][0] + entries
            num_hours = ridership[weather][1] + 1
            ridership[weather] = [entries, num_hours]
        else:
            # start counting num hours, therefore start with 1
            ridership[weather] = [entries, 1]

    for weather in ridership:
        
        total_entries_per_weather = ridership[weather][0]
        total_hours_per_weather = ridership[weather][1]
        avg_entries_hourly = total_entries_per_weather / total_hours_per_weather
        print "{0}\t{1}".format(weather, avg_entries_hourly)


reducer()
