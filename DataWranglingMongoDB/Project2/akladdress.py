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

def retrieve_streets():
    pipeline = [ {'$group': {'_id': '$address.street',
                               'count': { '$sum': 1} }},
                 {'$sort': {'count': -1}},
                 {'$limit': 100} ]
    return pipeline

def retrieve_cities():
    pipeline = [ {'$group': {'_id': '$address.city',
                               'count': { '$sum': 1} }},
                 {'$sort': {'count': -1}},
                 {'$limit': 100} ]
    return pipeline

def aggregate(db, pipeline):
    # osm auckland data is in the 'full' collection
    result = db.full.aggregate(pipeline)
    return result

if __name__ == '__main__':
    # access the db auckland with osm data on auckland
    db = get_db('auckland')
    # pipeline_street = retrieve_streets()    
    # result_street = aggregate(db, pipeline_street)
    # pprint.pprint(result_street)

    pipeline_city = retrieve_cities()
    result_city = aggregate(db, pipeline_city)
    pprint.pprint(result_city)
    