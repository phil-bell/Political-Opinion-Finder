# This file connects to the MongoDB using the pymongo library.

import pymongo
from pymongo import MongoClient

class mongo:

    # function that is called to connect to the MongoDB, it returns an
    # an operator to send commands to the DB with
    def conn(self):
        self.client = MongoClient() #sets the client (is local DB so no DB URL)
        self.db = self.client.tweetsDB #creates an operator for accessing the DB 
        return self.db #retruns the operator