#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    # we want you to split the input file into separate files
    # each containing a single patent.
    # As a hint - each patent declaration starts with the same line that was causing the error
    # The new files should be saved with filename in the following format:
    # "{}-{}".format(filename, n) where n is a counter, starting from 0.
    with open(filename, 'r') as f:
        
        # set counters to determine where to split file
        # N.B. all lines have a newline break when read in with f.readlines()
        begin = '<?xml version="1.0" encoding="UTF-8"?>\n'
         # Create an empty list to store all indices indicating start of XML file
        line_index = []

        read = f.readlines()
    
        # Step through whole XML, pulling out the index for start of file
        for i, line in enumerate(read):
            # If the current line matches beginning of XML file...
            if line == begin:
                # ...append the index to the list
                line_index.append(i)

        # print line_index


        # with the index, able to write the split XML data to new files
        # for loop to set the counter
        for i in range(len(line_index)):

            # set the new filename format
            fname = "{}-{}".format(filename, i)
            print fname

            start_pos = line_index[i]
            # index i starts at 0
            if i < len(line_index) - 1:
                # if not the last XML data structure, end of structure is indexed by
                # beginning of next structure, subtracted by 1
                end_pos = line_index[i+1] - 1
            else:
                # if it's the last data structure, then the end position 
                # of the data struture will be end of the file
                end_pos = len(read)
            # print 'start= ', start_pos, 'end= ', end_pos


            with open(fname, 'w') as newfile:
                for j, line in enumerate(read):
                    if j >= start_pos and j <= end_pos: 
                        newfile.write(line)

def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()