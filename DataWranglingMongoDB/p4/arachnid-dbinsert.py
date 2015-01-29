import json

def insert_data(data, db):

    # Loop through the list and for every dict, insert into MongoDB 
    # collections arachnid
    for e in data:
        db.arachnid.insert(e)


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()