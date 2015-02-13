#!/usr/bin/env python
""" Your task is to write a query that will return all cities
that are founded in 21st century.
Please modify only 'range_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""
from datetime import datetime
    
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def range_query():
    query = {'foundingDate': {'$gte': datetime(2001, 1, 1, 0, 0),
                              '$lte': datetime(2099, 12, 31, 0 ,0)} }
    return query


if __name__ == "__main__":

    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print "Found cities:", cities.count()
    import pprint
    pprint.pprint(cities[0])
