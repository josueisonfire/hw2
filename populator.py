from pymongo import MongoClient
mongo_client = MongoClient()
import json
import os

print(mongo_client.list_database_names())


mydb = mongo_client["hw2"]
factbook = mydb["factbook"]

curr_dir = os.getcwd()

json_dir = os.path.join(curr_dir, "all_.jsons/")

print(json_dir)

for filename in os.listdir(json_dir):
    #Obtain File Path.
    file_path = os.path.join(json_dir, filename)
    with open(file_path, "r") as f:
        json_data = f.read()
        print("N  E  X  T          D  A  T  A  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      I    N :%s" %filename)
        # print(json_data)
        # convert into dict.
        dict_data = json.loads(json_data)
        # print(dict_data)
        _id = factbook.insert_one(dict_data)
        print(_id)


