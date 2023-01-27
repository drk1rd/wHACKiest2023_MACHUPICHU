import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://root:toor@cluster0.r8i6ufr.mongodb.net/?retryWrites=true&w=majority') #connects to database

db=cluster['lmdb']
collection=db['users']



def ftod(a,b):
    post = {"name":a,"sport":b}
    collection.insert_one(post)
