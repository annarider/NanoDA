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

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
suburb_re = re.compile(r'^([a-zA-Z ]*)(,|$)')
auck_re = re.compile(r'^([Auckland])*$')

# use the OSM Auckland data
OSMFILE = "osm-auckland.xml"

def audit_city(cityname, city_types, count_auckland):
    if cityname != 'Auckland':
        if cityname not in city_types:
            city_types[cityname] = 1
        else: 
            city_types[cityname] += 1
    # count number of correct city values where city is 'Auckland' 
    elif cityname == 'Auckland': 
        count_auckland += 1
            
    return city_types, count_auckland

def is_city(elem):
    return (elem.attrib['k'] == "addr:city")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    # set to see all the variations on the city 'Auckland'
    city_types = {}
    count_auckland = 0
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_city(tag):
                    city_types, count_auckland = audit_city(tag.attrib['v'], city_types, count_auckland)
    print "number of occurances of 'Auckland' = ", count_auckland
    audit_data(city_types)
    return city_types

def clean_city(cityname):
    suburb = None
    m = suburb_re.search(cityname)
    if m: 
        suburb = m.group(1)
        n = auck_re.search(suburb)
        if n:
            suburb = None
        # hard coded city to Auckland because I am only dealing with the Auckland metro area
    return 'Auckland', suburb


def audit_data(city_types):
    # iterate through all dirty cities, retrieve suburbs if available, and correct to 'Auckland' 
    for city in city_types:
        correct_city, suburb = clean_city(city)
        print city, "=>", correct_city
        # print 'suburb => ', suburb
        print city, "=>", suburb



if __name__ == '__main__':
    print audit(OSMFILE)