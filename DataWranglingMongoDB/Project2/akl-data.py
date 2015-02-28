#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
# from akl-audit import update_name

"""
Regex for testing for problematic characters and expected values
"""

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

''' 

'''

def shape_element(element):
    node = {}
    # instantiate 'created' dict to start storing 'created' attributes
    created = {}
    # create pos list in preparation to store lat & long
    pos = ['lat','lon']
    if element.tag == "node" or element.tag == "way" :
        attributes = element.attrib

        # add the element type to node
        node['type'] = element.tag
        # start iterating through attributes and assigning to node
        for attr in attributes:

            # test if attribute needs to go under 'created' dict
            if attr in CREATED:
                created[attr] = attributes[attr]
                # add 'created' dict to node
                node['created'] = created

            # process first level of elements, e.g 'id', 'type', 'visible'
            node = process_element(node, attributes, attr, pos)
            
            # process child elements, e.g. 'tag' in 'node' and 'nd' in 'way' for address data and node_ref data
            node = process_child_element(node, element)
        
        return node
    else:
        return None

def process_element(node, attributes, attr, pos):

    # save id, type, & visible attributes directly into node dict
    if attr == 'id':
        node['id'] = attributes[attr]
    if attr == 'type':
        node['type'] = attributes[attr]
    if attr == 'visible':
        node['visible'] = attributes[attr]

    # save attributes pos, amenity, cuisine, name, or phone to node dict
    # test for lat & lon to save in pos then save pos to node
    if attr == 'lat':
        pos[0] = float(attributes[attr])
        node['pos'] = pos       # saving pos now avoids saving pos = ['lat', 'lon']
    if attr == 'lon':
        pos[1] = float(attributes[attr])
        node['pos'] = pos

    return node

def process_child_element(node, element,):
    # instantiate 'address' dict to start storing address attributes
    address = {}
    # instantiate 'node_refs' list to start storing node references
    node_refs = []

    # if 'node' has child 'tag' or 'way has child 'nd', iterate through to extract address and location data
    for child in element:
    
        # process attributes within 'tag', first check for tag which is nested in 'node'
        if child.tag  == 'tag':
            
            node = process_address(node, address, child)    
            
        # process attributes within 'nd', first check for 'nd' which is nested in 'way'
        if child.tag  == 'nd':
            # assign nd values to k and v
            # retrieve the value of 'nd', e.g. 'ref': '2636086177'
            # extract the value from the key-value pair to only have the reference number
            ref_val = child.attrib['ref']
            # add the value of 'nd' to the node_refs list
            node_refs.append(ref_val)
        # add list of 'node_refs' to 'node' dict
        node['node_refs'] = node_refs

    return node

def process_address(node, address, child):
    # assign tag values to k and v
    k, v = child.attrib['k'], child.attrib['v']

    # check for problematic characters, if problematic, ignore that tag
    if problemchars.search(k) == None:

        # save these below attributes to node, not address
        if k == 'amenity':
            node['amenity'] = v
        if k == 'cuisine':
            node['cuisine'] = v
        if k == 'name':
            node['name'] = v
        if k == 'phone':
            node['phone'] = v

        # test for address tags
        if 'addr:' in k and lower_colon.search(k) != None:
            # check for second level of ':', ignore tag if found 
            if 'addr:street:' not in k:
                start_colon = k.find(':')
                # extract the word after 'addr:' to use as key in address dict
                # add 1 to start of colon to avoid the ':'
                tag = k[start_colon+1:]
                address[tag] = v
                # print address
    node['address'] = address
    return node

def create_json_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "osm-auckland.json"
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def process_map():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the create_json_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    data = create_json_map("osm-auckland.xml", False)
    pprint.pprint(data)
    

if __name__ == "__main__":
    process_map()