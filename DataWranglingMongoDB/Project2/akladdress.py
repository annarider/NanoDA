'''
Intro: This script queries the MongoDB db auckland, collection full to retrieve
the osm data on Auckland after it has been preliminarily cleaned, transformed
into JSON, and imported into MongoDB.

The queries return information such as a list of all possible cities and streets
to ensure consistent data values.  
'''

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [ {'$group': {'_id': '$address.street',
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
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
    