import pprint
from pymongo import MongoClient
'''
Intro: This script queries the MongoDB db auckland, collection full to retrieve
the osm data on Auckland after it has been preliminarily cleaned, transformed
into JSON, and imported into MongoDB.

The queries return information such as a list of all possible cities and streets
to ensure consistent data values.  
'''

def get_db(db_name):
    
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

'''
MongoDB query to return street address if not null, group the values by
street, and count the number of each street's occurences. The query
returns the most common street names first.
'''  
def retrieve_streets():
    pipeline = [ {'$match': {'address.street': {'$exists': 1}}},
                 {'$group': {'_id': '$address.street',
                               'count': { '$sum': 1} }},
                 {'$sort': {'count': -1}}]
    return pipeline

'''
MongoDB query to return city if not null, group the values by
city, and count the number of each city's occurences. The query
returns the most common cities first.
'''
def retrieve_cities():
    pipeline = [ {'$match': {'address.city': {'$exists': 1}}},
                 {'$group': {'_id': '$address.city',
                               'count': { '$sum': 1} }},
                 {'$sort': {'count': -1}}]
    return pipeline

'''
This query returns the number of address documents that are missing
a city but have at least a street
'''
def missing_cities():
    pipeline = [ {'$match': {'address': {'$exists': 1}}},
                 {'$match': {'address.street': {'$exists': 1}}},
                 {'$match': {'address.city': {'$exists': False}}},
                 {'$group': {'_id': '$address.city','count': { '$sum': 1} }} ]
    return pipeline

def aggregate(db, pipeline):
    # osm auckland data is in the 'full' collection
    result = db.full.aggregate(pipeline)
    return result

if __name__ == '__main__':
    # access the db auckland with osm data on auckland
    db = get_db('auckland')
    # set of street commands with aggregation pipeline query & pretty print streetnames
    # pipeline_street = retrieve_streets()    
    # result_street = aggregate(db, pipeline_street)
    # pprint.pprint(result_street)

    # set of city commands to aggregate city data and pretty print all cities in dataaset
    # pipeline_city = retrieve_cities()
    # result_city = aggregate(db, pipeline_city)
    # pprint.pprint(result_city)

    # set of city commands to aggregate city data and pretty print all cities in dataaset
    pipeline_missing_city = missing_cities()
    missing_city = aggregate(db, pipeline_missing_city)
    pprint.pprint(missing_city)

    