from flask import Flask, jsonify, request, json
from Basics import Fees
import pymongo
from bson import json_util
app = Flask(__name__)



client=pymongo.MongoClient("mongodb+srv://yash-mtalkz:12345@cluster0.xhm9l9v.mongodb.net/?retryWrites=true&w=majority")
db=client["Fees"]
coll = db['Deatails']

@app.route('/insert', methods =['POST'])
def insert():
    data=request.get_json()
    coll.insert_one(data)
    #client.close()
    return jsonify({"status":"Connection succesfull"}),200


@app.route('/', methods =['GET'])
def show():
    documents=coll.find()
    response=[]
    for document in documents:
        document["_id"]=str(document["_id"])
        response.append(document)
    return json.dumps(response,indent=4,default=json_util.default)

@app.route('/update/<string:name>',methods=['PUT'])
def update(name):
    query={"name":name}
    data=request.get_json()
    new_query={"$set":{"name":data["name"]}}
    query=coll.update_one(query,new_query)
    return jsonify({"Status":"Connection Successful"}),200




@app.route('/delete/<string:name>',methods=['DELETE'])
def delete(name):
    query={"name":name}
    coll.delete_one(query)
    return jsonify({"status":"Connection successful"})



if __name__ == ('__main__'):
    app.run(debug=True, port=8888)
