#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it, 
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.
Your task in this exercise is to parse the file, process only the fields that are listed in the
FIELDS dictionary as keys, and return a dictionary of cleaned values. 

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
  eg removing "*" prefixes etc
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}
  * Note that the value associated with the classification key is a dictionary with
    taxonomic labels.
"""
import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


def process_file(filename, fields):

    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            cleaned = clean_line(line, fields)
            # print cleaned
            data.append(cleaned)
    return data

def clean_line(line, fields):
  # store all the new keys from the mapping of FIELDS
  clean_data = {}

  for key in line:
    if key in fields:
      # strips all whitespace from the values
      # maps the current key to the new key and saves in variable to comparisons 
      new_key = fields[key].strip()
      # strips all whitespaces from the 
      clean_data[new_key] = line[key].strip()
      # print 'key= ', new_key, 'value= ', clean_data[new_key]

      ### Begin systematic cleaning based on criteria listed above

      # 1. Trim redundant descriptions from label 
      if new_key == 'label':
        clean_data[new_key] = trim_label(line[key])
        # print 'key= ', new_key, 'value= ', clean_data[new_key]

      # 2. Check if name is null or non-ASCII, convert to label
      if new_key == 'name':

        clean_data[new_key] = line[key]
        clean_data[new_key] = clean_name(line[key], trim_label(line['rdf-schema#label']))
        # print trim_label(line['rdf-schema#label'])
        # print 'key= ', new_key, 'value= ', clean_data[new_key]
        # print clean_data

      # 3. If a value field is 'NULL', make the value equal to None

      if line[key] == 'NULL':
        # print clean_data[new_key]

        clean_data[new_key] = None
      # print clean_data

      print clean_data
      # 4. Converting values in synonyms to lists
      if clean_data[new_key] is not None:
        clean_data[new_key] = convert_to_list(line[key])

  # print clean_data

'''
When the key is a label, this method checks if there is a
redundant description in parentheses. If yes, then it removes the 
description, if not, then it returns the original value.
'''

def trim_label(value):
  if '(' in value or ')' in value: 
    pos = value.find('(')
    return value[:pos]
  else: 
    return value

'''
Clean up the name value. If 'NULL' or non-alphanumeric, make same
as label, otherwise, keep the value. 
'''
def clean_name(value, label):
  if value == 'NULL':
    # print 'value= ', value, 'label=', label
    return label
    # from python regex docs: If the first character of the set is '^', 
    # all the characters that are not in the set will be matched.
  if re.match('^[\w-]+$', value) is not None:
    return label
  else: 
    return value


'''
Clean all synonyms so the values are stored in a list
'''
def convert_to_list(value):
  # check to make sure the value is actually an array
  if '{' in value or '{' in value:
    # first remove the curly braces, then split on pipe
    synonym = value[1:-1].split('|')
    return synonym
  # if not array but just one synonym, then return the original value
  else:
    value


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)

    pprint.pprint(data[0])
    # assert data[0] == {
    #                     "synonym": None, 
    #                     "name": "Argiope", 
    #                     "classification": {
    #                         "kingdom": "Animal", 
    #                         "family": "Orb-weaver spider", 
    #                         "order": "Spider", 
    #                         "phylum": "Arthropod", 
    #                         "genus": None, 
    #                         "class": "Arachnid"
    #                     }, 
    #                     "uri": "http://dbpedia.org/resource/Argiope_(spider)", 
    #                     "label": "Argiope", 
    #                     "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    #                 }


if __name__ == "__main__":
    test()