# This file connects to the MongoDB using the pymongo library.

import pymongo
from pymongo import MongoClient

# function that is called to connect to the MongoDB, it returns an
# an operator to send commands to the DB with
def conn():
    client = MongoClient("""inserts DB URL here""") #sets the client (is local DB so no DB URL)
    db = client.tweetsDB #creates an operator for accessing the DB 
    return db #retruns the operator