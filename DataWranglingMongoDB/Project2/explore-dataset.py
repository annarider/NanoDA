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
    result = db.auckland.aggregate(pipeline)
    return result

'''
Queries for stats on users_results
'''
# list all users in descending order based on number of contributions
def list_users():
    users_pipeline = [{'$group': {'_id': '$created.user', 'count': {'$sum': 1}}},
                      {'$sort': {'count': -1}},
                      {'$limit': 3}]
    users_results = aggregate(db, users_pipeline)
    pp.pprint(users_results)

# returns the number of unique users 
def unique_users():
    users_pipeline = [{'$group': {'_id': '$created.user'}},
                      {'$group': {'_id': 'Users', 'count': {'$sum': 1}}}]
    users_results = aggregate(db, users_pipeline)
    pp.pprint(users_results)

def list_amenities():
    amenities = db.auckland.aggregate([{'$match': {'amenity': {'$exists': 1}}},
                                       {'$group': {'_id': '$amenity', 'count': {'$sum': 1}}},
                                       {'$match': {'count': {'$gte': 100}}},
                                       {'$sort': {'count': -1}}])
    print amenities
    pp.pprint(amenities)

if __name__ == '__main__':
    db = get_db('osm')
    # list_users()
    # unique_users()
    list_amenities()