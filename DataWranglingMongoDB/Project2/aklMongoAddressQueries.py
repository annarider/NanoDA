'''
Intro: This script queries the MongoDB db 'auckland', collection 'full' to retrieve
the osm data on Auckland, after it was cleaned, standardized, transformed
into JSON, and imported into MongoDB.

These sets of queries return address-related information, 
such as a list of all possible cities, streets, and postcodes.
'''
import pprint
from pymongo import MongoClient

def get_db(db_name):
    
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def aggregate(db, pipeline):
    # osm auckland data is in the 'full' collection
    result = db.full.aggregate(pipeline)
    return result


'''
MongoDB query to return street address if not null, group the values by
street, and count the number of each street's occurences. The query
returns the most common street names first.
'''  
def retrieve_streets():
    # set of street commands with aggregation pipeline query & pretty print streetnames
    pipeline_street = [ {'$match': {'address.street': {'$exists': 1}}},
                 {'$group': {'_id': '$address.street',
                               'count': { '$sum': 1} }},
                 {'$sort': {'count': -1}}]
    result_street = aggregate(db, pipeline_street)
    pprint.pprint(result_street)


'''
MongoDB query to return city if not null, group the values by
city, and count the number of each city's occurences. The query
returns the most common cities first.
'''
def retrieve_cities():
    # set of city commands to aggregate city data and pretty print all cities in dataaset
    pipeline_city = [ {'$match': {'address.city': {'$exists': 1}}},
                 {'$group': {'_id': '$address.city',
                               'count': { '$sum': 1} }},
                 {'$sort': {'count': -1}}]
    result_city = aggregate(db, pipeline_city)
    pprint.pprint(result_city)


'''
This query returns the number of address documents that are missing
a city but have at least a street
'''
def missing_cities():
    # set of city commands to aggregate city data and pretty print all cities in dataaset
    pipeline_missing_city = [ {'$match': {'address': {'$exists': 1}}},
                 {'$match': {'address.street': {'$exists': 1}}},
                 {'$match': {'address.city': {'$exists': False}}},
                 {'$group': {'_id': '$address.city','count': { '$sum': 1} }} ]
    missing_city = aggregate(db, pipeline_missing_city)
    pprint.pprint(missing_city)

'''
This query returns the all suburbs in Auckland dataset
'''
def retrieve_suburbs():
    # set of city commands to aggregate city data and pretty print all cities in dataaset
    pipeline_suburb = [ {'$match': {'address': {'$exists': 1}}},
                 {'$match': {'address.suburb': {'$exists': 1}}},
                 {'$group': {'_id': '$address.suburb','count': { '$sum': 1} }} ]
    suburbs = aggregate(db, pipeline_suburb)
    pprint.pprint(suburbs)

'''
This query returns the all postal codes in Auckland dataset
'''
def retrieve_postcode():
    # set of city commands to aggregate city data and pretty print all cities in dataaset
    pipeline_postcode = [ {'$match': {'address': {'$exists': 1}}},
                 {'$match': {'address.postcode': {'$exists': 1}}},
                 {'$group': {'_id': '$address.postcode','count': { '$sum': 1} }}, 
                 {'$sort': {'count': -1}}]
    postcodes = aggregate(db, pipeline_postcode)
    pprint.pprint(postcodes)

if __name__ == '__main__':
    # access the db auckland with osm data on auckland
    db = get_db('auckland')
    # retrieve_cities()
    retrieve_streets()
    # missing_cities()
    # retrieve_suburbs()
    # retrieve_postcode()



    