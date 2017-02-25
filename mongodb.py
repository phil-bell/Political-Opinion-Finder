def conn():
    client = MongoClient()
    db = client.tweetsDB
    return db