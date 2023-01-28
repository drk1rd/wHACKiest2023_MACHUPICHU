import pymongo
from pymongo import MongoClient
from flask import jsonify
import os
from dotenv import load_dotenv
load_dotenv()
MONGO = os.getenv('MONGO')

cluster = MongoClient(MONGO) #connects to database

db=cluster['lmdb']
collection=db['users']



def dtof(a):
    user=collection.find({"sport":a})
    userl=[]
    for x in user:
        userl.append(x["name"])
    return userl
