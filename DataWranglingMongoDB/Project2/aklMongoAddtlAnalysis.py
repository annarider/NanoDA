'''
Intro: This script contains queries for additional analysis
of the OSM Auckland dataset, such as the most common
sports and tourism points in the city.
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
# list main sport facilities in descending order
def list_sports():
    sport_pipeline = [{'$match': {'sport': {'$exists': 1}}},
    {'$group': {'_id': '$sport', 'count': {'$sum': 1}}},
                      {'$sort': {'count': -1}} ] #,{'$limit': 5}]
    sports_results = aggregate(db, sport_pipeline)
    pp.pprint(sports_results)

# lists cuisines found in Auckland in descending order
def top_cuisines():
    cuisine = db.auckland.aggregate([{'$match': {'cuisine': {'$exists': 1}}},
                                       {'$group': {'_id': '$cuisine', 'count': {'$sum': 1}}},
                                       {'$sort': {'count': -1}}])
    pp.pprint(cuisine)

# lists tourism facilities found in Auckland in descending order
def list_tourism():
    tourism = db.auckland.aggregate([{'$match': {'tourism': {'$exists': 1}}},
                                       {'$group': {'_id': '$tourism', 'count': {'$sum': 1}}},
                                       {'$sort': {'count': -1}}])
    pp.pprint(tourism)

# lists shops found in Auckland in descending order
def list_shop():
    shop = db.auckland.aggregate([{'$match': {'shop': {'$exists': 1}}},
                                       {'$group': {'_id': '$shop', 'count': {'$sum': 1}}},
                                       {'$sort': {'count': -1}}])
    pp.pprint(shop)

# lists buildings found in Auckland in descending order
def list_building():
    building = db.auckland.aggregate([{'$match': {'building': {'$exists': 1}}},
                                       {'$group': {'_id': '$building', 'count': {'$sum': 1}}},
                                       {'$sort': {'count': -1}}])
    pp.pprint(building)

# lists buildings found in Auckland in descending order
def list_offices():
    offices = db.auckland.aggregate([{'$match': {'office': {'$exists': 1}}},
                                       {'$group': {'_id': '$office', 'count': {'$sum': 1}}},
                                       {'$sort': {'count': -1}}])
    pp.pprint(offices)

# Query to return all information about Les Mills gyms
def find_lesmills():
    gyms = db.auckland.find({'name': 'Les Mills'})
    for g in gyms:
        pp.pprint(g)

if __name__ == '__main__':
    db = get_db('osm')
    # list_sports()
    # top_cuisines()
    # list_tourism()
    # list_shop()
    list_building()
    # find_lesmills()
    # list_offices()