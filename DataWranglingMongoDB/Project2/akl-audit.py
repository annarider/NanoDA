"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "osm-auckland.xml"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
# add another regex to match for directions
street_direction_re = re.compile(r'\b\S+\.?^', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Crescent", "Way"]
directions = ['North', 'South', 'East', 'West', 'north']

# updated the mapping by adding more unusual street name endings to standardize to expected values
mapping = { 'St': 'Street',
            'St.': 'Street',
            'street': 'Street',
            'st': 'Street',
            'Ave': 'Avenue',
            'Rd.': 'Road',
            'Rd': 'Road'}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def audit_street_direction(street_types, street_name):
    # n = street_direction_re.search(street_name)
    # if n:
    #     street_dir = n.group()
    #     if street_dir in directions:
    #         print street_name
    street = street_name.split(' ', 1)[0]
    if street in directions:
        print street_name


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
                    audit_street_direction (street_types, tag.attrib['v'])

    return street_types


def update_name(name, mapping):
    # retrieve the street type e.g. Ave or St.
    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        # test if street type is in group of unexpected types by checking key against mapping
        if street_type in mapping:
            # street type is unexpected
            # find the beginning position of street type in street name
            start_pos = m.start()
            name = name[:start_pos] + mapping[street_type] 
    return name


def audit_data():
    st_types = audit(OSMFILE)
    # pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            # print name, "=>", better_name


if __name__ == '__main__':
    audit_data()