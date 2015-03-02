'''
Intro: This script is written to clean city data. 
The main problems to address are: 
1. Ensure the correct spelling of Auckland and consistent 
capitalization
2. If a suburb is present in the city value, return the
suburb separately from the city so that the suburb can 
have its own key-value pair in the JSON file to be imported
into MongoDB
3. Check street field to determine if there is city information
(including checking for numbers and punctuation like commas)
'''
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
from pymongo import MongoClient
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def get_db(db_name):
    
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def aggregate(db, pipeline):
    # osm auckland data is in the 'full' collection
    result = db.full.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('auckland')