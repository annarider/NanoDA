'''
Intro: This script contains queries for exploring the OSM Auckland
dataset in MongoDB. It differs from the aklMongoAddressQueries.py 
in that it is not used so much for auditing the dataset but 
rather to find interesting features such as different amenities and
meta-properties like the number of unique users.
'''

from pymongo import MongoClient
import pprint as pp


def get_db(db_name):
    # osm auckland data is stored in db 'auckland'
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def aggregate(db_name, pipeline):
    # osm auckland data is in the 'full' collection
    result = db.full.aggregate(pipeline)
    return result

def num_users():
    users_pipeline = [{'$group': {'_id': '$created.user', 'count': {'$sum': 1}}},
                      {'$sort': {'count': -1}}]
    users_results = aggregate(db, users_pipeline)
    pp.pprint(users_results)



if __name__ == '__main__':
    db = get_db('auckland')
    num_users()