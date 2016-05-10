import pymongo
import json
import os
import gc
from os import walk
from random import randint
from pyexcel_xlsx import get_data

base='http://www.filterlady.com/'

def MongoDBconnection(database, collection):
  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection[database]
  cursor = db[collection]
  return connection, db, cursor

def getProductImages(pid):
  try:
    ids = pid.split("_")
    path = os.getcwd()+"/Product/static/Products/"+ ids[1]+ '/'+ ids[2]+ "/"+ ids[3]+ "/"+ids[4]+"/"
    images = list()
    if os.path.isdir(path):
      if os.listdir(path) and os.listdir(path):
	for f in os.listdir(path):
	  images.append("/Product/static/Products/"+ ids[1]+ '/'+ ids[2]+ "/"+ ids[3]+ "/"+ids[4]+"/"+f)
      else:
	images.append("/Product/static/Products/NA.jpg")
    else:
      images.append("/Product/static/Products/NA.jpg")
    return images
  except Exception as e:
    print str(e)
    return []

def retrieveAllProducts(level1Category):
  try:
    level1Category = level1Category.replace(" ","_")
    connection, db, collection = MongoDBconnection('Admin', 'Categories')
    iter = collection.find({'_id':level1Category})
    categories = iter[0]['Categories']
    products = list()
    for category in categories:
      for mainCategory in category:
	for subCategory in category[mainCategory]:
	  products.append(categoryProducts(level1Category, mainCategory, subCategory))
    connection.close()
    gc.collect()
    return str(json.dumps(products))
  except Exception as e:
    print str(e)
    return 'Unable to Fetch'

def categoryProducts(level1Category, MainCategory, SubCategory):
  try:
    level1Category = level1Category.replace(" ","_")
    MainCategory = MainCategory.replace(" ","_")
    SubCategory = SubCategory.replace(" ","_")
    connection, db, collection = MongoDBconnection(MainCategory, SubCategory)
    iter = collection.find()
    products = list()
    if not iter.count():
      return '[]'
    for i in iter:
      i['images'] = getProductImages(i['_id'])
      products.append(i)
    connection.close()
    gc.collect()
    return str(json.dumps(products))
  except Exception as e:
    print str(e)
    return 'Unable to Fetch'
  
def categoryProductDetail(level1Category, MainCategory, SubCategory, pid):
  try:
    level1Category = level1Category.replace(" ","_")
    MainCategory = MainCategory.replace(" ","_")
    SubCategory = SubCategory.replace(" ","_")
    connection, db, collection = MongoDBconnection(MainCategory.replace(" ","_"), SubCategory.replace(" ","_"))
    iter = collection.find({"_id":pid})
    products = list()
    if not iter.count():
      return '[]'
    for i in iter:
      i['images'] = getProductImages(i['_id'])
      products.append(i)
    connection.close()
    gc.collect()
    return str(json.dumps(products))
  except Exception as e:
    print str(e)
    return 'Unable to Fetch'

def newProducts(level1Category, MainCategory, SubCategory):
  try:
    level1Category = level1Category.replace(" ","_")
    MainCategory = MainCategory.replace(" ","_")
    SubCategory = SubCategory.replace(" ","_")
    connection, db, collection = MongoDBconnection(MainCategory.replace(" ","_"), SubCategory.replace(" ","_"))
    iter = collection.find()
    products = list()
    if not iter.count():
      return '[]'
    for i in iter:
      i['images'] = getProductImages(i['_id'])
      products.append(i)
    products= products[::-1]
    connection.close()
    gc.collect()
    return str(json.dumps(products))
  except Exception as e:
    print str(e)
    return 'Unable to Fetch'

def randomSubCategory(id, mainCategory, mainCategoryIndex):
  connection, db, collection = MongoDBconnection('Admin', 'Categories')
  iter = collection.find({"_id":id})
  subCategoryIndex = randint(0,len(iter[0]['Categories'][mainCategoryIndex][mainCategory])-1)
  subCategory = iter[0]['Categories'][mainCategoryIndex][mainCategory][subCategoryIndex]
  connection.close()
  gc.collect()
  return subCategory, subCategoryIndex

def randomCategory(id):
  connection, db, collection = MongoDBconnection('Admin', 'Categories')
  iter = collection.find({"_id":id})
  randnumber = randint(0,len(iter[0]['Categories']) -1)
  categories = iter[0]['Categories']
  mainCategory = categories[randnumber]
  subCategory, subCategoryIndex = randomSubCategory(id, mainCategory.keys()[0], randnumber)
  connection.close()
  gc.collect()
  return mainCategory.keys()[0], randnumber, subCategory, subCategoryIndex

def randomProducts(id):
  mainCategory, mainCategoryIndex, subCategory, subCategoryIndex = randomCategory(id)
  print mainCategory, mainCategoryIndex, subCategory, subCategoryIndex
  return categoryProducts(id, mainCategory, subCategory)

def randomMainCategoryProducts(id, mainCategory):
  connection, db, collection = MongoDBconnection('Admin', 'Categories')
  iter = collection.find({"_id":id})
  for index, category in enumerate(iter[0]['Categories']):
    if mainCategory == category.keys()[0]:
      mainCategoryIndex = index
      break
  subCategory, subCategoryIndex = randomSubCategory(id, mainCategory, mainCategoryIndex)
  connection.close()
  gc.collect()
  return categoryProducts(id, mainCategory, subCategory)

def searchProduct(level1Category):
  try:
    connection, db, collection = MongoDBconnection('Admin', 'Categories')
    iter = collection.find({"_id":level1Category})
    results = list()
    for index, mainCategory in enumerate(iter[0]['Categories']):
      for c in mainCategory:
	print 
	for subCategory in mainCategory[c]:
	  connection.close()
	  gc.collect()
	  connection, db, collection = MongoDBconnection(c.replace(" ","_"), subCategory.replace(" ","_"))
	  iter = collection.find()
	  if iter.count():
	    for i in iter:
	      print i['_id'], i['product_name']
    connection.close()
    gc.collect()
    return json.dumps(results)
  except Exception as e:
    return '{"response":"Unable to Retrieve"}'
  
def registerProduct(MainCategory, SubCategory, product):
  try:
    MainCategory = MainCategory.replace(" ","_")
    SubCategory = SubCategory.replace(" ","_")
    product = json.loads(product)
    connection, db, collection = MongoDBconnection(MainCategory, SubCategory)
    iter = collection.find()
    if not iter.count():
      product['_id']='P'+product['_id']+'_1'
    else:
      product['_id'] = 'P'+product['_id']+'_'+ str(int(iter[iter.count()-1]['_id'].split("_")[-1])+1)
    collection.insert(product)
    connection.close()
    gc.collect()
    return 'Registered', product['_id']
  except Exception as e:
    return str(e), ''
    return 'Unable to Register', '[]'

def registerBulkProduct(tableName,fileName):
  try:
    records = get_data(fileName)
    i = 1
    while i < len(records) and i<11:
      product = {'product_name':records[i][0], 'Actual_Price':records[i][1], 'TMS_Price':records[i][2], 'Shop_Name': tableName, '_id':''}
      i=i+1
      reply= registerProduct('TMS', tableName, str(json.dumps(product)))
      #if reply == 'Registered' and pid:
	#ProductImagePath(pid)
    gc.collect()
    return 'Registered'
  except Exception as e:
    return str(e)
    return 'Unable to Register', '[]'

if __name__ == "__main__":
  print registerBulkProduct('PGI1','pgi_data.xlsx')
  #print randomProducts('Grocery')
  #searchProduct('Grocery')
  #print retrieveAllProducts('Grocery')
  #print randomMainCategoryProducts('Grocery', 'Beverages and Drinks')
  #print categoryProducts('Grocery', 'Cereals', 'Cornflakes')
  #print newProducts('Grocery', 'Bakery', 'Cakes')
