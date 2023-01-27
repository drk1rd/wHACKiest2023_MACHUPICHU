import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://root:toor@cluster0.r8i6ufr.mongodb.net/?retryWrites=true&w=majority') #connects to database

db=cluster['lmdb']
collection=db['users']



name = input("enter your name: ")
sport = int(input("enter sport:\n1.Football\n2.Basketball\n3.Badminton\n"))
if sport==1:
    sports = 'Football'
elif sport==2:
    sports = 'Basketball'
elif sport==3:
    sports='Badminton'
else:
    print("error")
post = {"name":name,"sport":sports}
collection.insert_one(post)

