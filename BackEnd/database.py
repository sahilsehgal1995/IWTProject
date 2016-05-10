import pymongo
import json
import os
import gc
from os import walk
import datetime
from passlib.hash import sha256_crypt
from random import randint

def MongoDBconnection(database, collection):
  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection[database]
  cursor = db[collection]
  return connection, db, cursor

def Fetchstudents():
  try:
    connection, db, collection = MongoDBconnection('IWT', 'Students')
    iter = collection.find({},{"_id":False})
    orders = list()
    for order in iter:
      orders.append(order)
    connection.close()
    gc.collect()
    return json.dumps(orders)
  except Exception as e:
    print str(e)
    return 'Unable to Place order'
  
def FetchSyllabus():
  try:
    connection, db, collection = MongoDBconnection('IWT', 'syllabus')
    iter = collection.find({},{"_id":False})
    orders = list()
    for order in iter:
      orders.append(order)
    connection.close()
    gc.collect()
    return json.dumps(orders)
  except Exception as e:
    print str(e)
    return 'Unable to Place order'

def FetchTeachers():
  try:
    connection, db, collection = MongoDBconnection('IWT', 'teachers')
    iter = collection.find()
    orders = list()
    for order in iter:
      orders.append(order)
    connection.close()
    gc.collect()
    return json.dumps(orders)
  except Exception as e:
    print str(e)
    return 'Unable to Place order'

def registerTeacher(user):
  try:
    connection, db, collection = MongoDBconnection('IWT', 'Admin')
    user = json.loads(user)
    if collection.find({'$or':[{"Mobile":user['Mobile']},{"Email":user['Email']}]}).count():
      return 'User Already Exists'
    iter = collection.find()
    if not iter.count():
      user['_id']='A_1'
    else:
      user['_id'] = 'A_'+ str(int(iter[iter.count()-1]['_id'].split("_")[-1])+1)
    user['Password']= sha256_crypt.encrypt(str(user['Password']))
    collection.insert(user)
    connection.close()
    gc.collect()
    return 'Registration Successfull'
  except Exception as e:
    print str(e)
    return 'Unable to Register'

def loginTeacher(user):
  try:
    connection, db, collection = MongoDBconnection('IWT', 'Admin')
    user = json.loads(user)
    iter = collection.find({'$or':[{"Email":user['Email']},{"Mobile":user['Mobile']}]})
    if not iter.count():
      return "User Does't Exists", '[]'
    print iter[0]['Password']
    if sha256_crypt.verify(user['Password'],iter[0]['Password']):
      reply = iter[0]
      connection.close()
      gc.collect()
      del reply['Password']
      connection.close()
      gc.collect()
      return 'Login Success', reply
    else:
      connection.close()
      gc.collect()
      return 'Authentication Failed', '[]'
  except Exception as e:
    return str(e)
    return 'Unable to Login', '[]'

if __name__ == "__main__":
  print ''
  