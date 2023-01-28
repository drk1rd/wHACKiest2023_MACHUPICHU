import pymongo
from pymongo import MongoClient


cluster = MongoClient('mongodb+srv://root:toor@cluster0.r8i6ufr.mongodb.net/?retryWrites=true&w=majority') #connects to database

db=cluster['lmdb']
collection=db['users']

fb_user=collection.find({"sport":"Football"})
bb_user=collection.find({"sport":"Basketball"})
bd_user=collection.find({"sport":"Badminton"})

football = []
basketball = []
badminton = []

for x in fb_user:
    football.append(x["name"])
for x in bb_user:
    basketball.append(x["name"])
for x in bd_user:
    badminton.append(x["name"])

print('football online\n')
fblist=print(*football, sep = "\n")
print('basketball online\n')
bblist=print(*basketball, sep = "\n")
print('badminton online\n')
bdlist=print(*badminton, sep = "\n")