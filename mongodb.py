import pymongo
from pymongo import MongoClient
def conn():
    client = MongoClient()
    db = client.tweetsDB
    return db