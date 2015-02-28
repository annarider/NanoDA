#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}

You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB. 

Note that in this exercise we do not use the 'update street name' procedures
you worked on in the previous exercise. If you are using this code in your final
project, you are strongly encouraged to use the code from previous exercise to 
update the street names before you save them to JSON. 

In particular the following things should be done:
- you should process only 2 types of top level tags: "node" and "way"
- all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    - attributes in the CREATED array should be added under a key "created"
    - attributes for latitude and longitude should be added to a "pos" array,
      for use in geospacial indexing. Make sure the values inside "pos" array are floats
      and not strings. 
- if second level tag "k" value contains problematic characters, it should be ignored
- if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
- if second level tag "k" value does not start with "addr:", but contains ":", you can process it
  same as any other tag.
- if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:

<tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>

  should be turned into:

{...
"address": {
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}

- for "way" specifically:

  <nd ref="305896090"/>
  <nd ref="1719825889"/>

should be turned into
"node_refs": ["305896090", "1719825889"]
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

''' 
This method does all the hard work checking the xml data and processes it to clean the 
map data. The goal is to prepare the data in a JSON format to import into mongodb
The code is a huge block because refactoring it into smaller functions made the code's
logic harder to follow. If you really want a refactored version, look for it in 
data-refactored.py
'''

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        attributes = element.attrib
        # instantiate 'created' dict to start storing 'created' attributes
        created = {}
        # instantiate 'address' dict to start storing address attributes
        address = {}
        # create pos list in preparation to store lat & long
        pos = ['lat','lon']

        # add the element type to node
        node['type'] = element.tag
        # start iterating through attributes and assigning to node
        for attr in attributes:

            # save id, type, & visible attributes directly into node dict
            if attr == 'id':
                node['id'] = attributes[attr]
            if attr == 'type':
                node['type'] = attributes[attr]
            if attr == 'visible':
                node['visible'] = attributes[attr]
            

            # test if attribute needs to go under 'created' dict
            if attr in CREATED:
                created[attr] = attributes[attr]
                # add 'created' dict to node
                node['created'] = created

            # save attributes pos, amenity, cuisine, name, or phone to node dict
            # test for lat & lon to save in pos then save pos to node
            if attr == 'lat':
                pos[0] = float(attributes[attr])
                node['pos'] = pos       # saving pos now avoids saving pos = ['lat', 'lon']
            if attr == 'lon':
                pos[1] = float(attributes[attr])
                node['pos'] = pos


            # instantiate 'node_refs' list to start storing node references
            node_refs = []

            # if 'node' has child 'tag' or 'way has child 'nd', iterate through to extract address and location data
            for child in element:
            
                # process attributes within 'tag', first check for tag which is nested in 'node'
                if child.tag  == 'tag':
                    
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
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
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

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    data = process_map('example3.osm', True)
    pprint.pprint(data)
    
    correct_first_elem = {
        "id": "261114295", 
        "visible": "true", 
        "type": "node", 
        "pos": [41.9730791, -87.6866303], 
        "created": {
            "changeset": "11129782", 
            "user": "bbmiller", 
            "version": "7", 
            "uid": "451048", 
            "timestamp": "2012-03-28T18:31:23Z"
        }
    }
    assert data[0] == correct_first_elem
    assert data[-1]["address"] == {
                                    "street": "West Lexington St.", 
                                    "housenumber": "1412"
                                      }
    assert data[-1]["node_refs"] == [ "2199822281", "2199822390",  "2199822392", "2199822369", 
                                    "2199822370", "2199822284", "2199822281"]

if __name__ == "__main__":
    test()