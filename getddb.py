from pymongo import MongoClient
import os
import urllib

uri = os.environ['MONGO_URI']
user = os.environ['MONGO_USER']
password = os.environ['MONGO_PASSWORD']

uri = uri.format( urllib.parse.quote_plus(user), urllib.parse.quote_plus(password))

# Create a new client and connect to the server
client = MongoClient(uri)

default_db = os.environ['MONGO_DB']
db = client[default_db]

useless_questions = ["hi", "hello", "Hi", "Hello", "Hey", "What up", "hey"]
# unanswered_questions 
# = []
f = open("C:/Users/varun/DTAI/mongo/unanswered_questions.txt", 'w')
count = 0
for item in db.qa_log.find():
    q = item['question']
    if q not in useless_questions :
        f.write(q+"\n")
        count += 1
        
f.close()


