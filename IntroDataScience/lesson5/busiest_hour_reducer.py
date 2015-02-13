import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Write a reducer that will compute the busiest date and time (that is, the 
    date and time with the most entries) for each turnstile unit. Ties should 
    be broken in favor of datetimes that are later on in the month of May. You 
    may assume that the contents of the reducer will be sorted so that all entries 
    corresponding to a given UNIT will be grouped together.
    
    The reducer should print its output with the UNIT name, the datetime (which 
    is the DATEn followed by the TIMEn column, separated by a single space), and 
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00    31213.0
    R002    2011-05-12 21:00:00    4295.0
    R003    2011-05-05 12:00:00    995.0
    R004    2011-05-12 12:00:00    2318.0
    R005    2011-05-10 12:00:00    2705.0
    R006    2011-05-25 12:00:00    2784.0
    R007    2011-05-10 12:00:00    1763.0
    R008    2011-05-12 12:00:00    1724.0
    R009    2011-05-05 12:00:00    1230.0
    R010    2011-05-09 18:00:00    30916.0
    ...
    ...

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    '''

    max_entries = 0
    datetime = ''

    busiest_units = {}

    for line in sys.stdin:
        data = line.strip().split("\t")

        unit, entries, date, time = data
        entries = float(entries)

        if unit in busiest_units:
            max_entries = busiest_units[unit][0]
            if entries > max_entries or entries == max_entries:
                busiest_units[unit] = [entries, date, time]
                
        else: 
            busiest_units[unit] = [entries, date, time]
        logging.info(busiest_units[unit])

    for unit in busiest_units:
        datetime = busiest_units[unit][1] + ' ' + busiest_units[unit][2]
        entries = busiest_units[unit][0]
        print "{0}\t{1}\t{2}".format(unit, datetime, entries)


reducer()
