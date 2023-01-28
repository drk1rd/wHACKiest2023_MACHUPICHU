import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
MONGO = os.getenv('MONGO')

cluster = MongoClient(MONGO) #connects to database

db=cluster['lmdb']
collection=db['users']



def ftod(a,b):
    post = {"name":a,"sport":b}
    collection.insert_one(post)
