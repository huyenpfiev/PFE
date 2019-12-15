from flask import Flask, request, json, g
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

#from DB import MongoRepository as db
from service import Service 
from schema import UserSchema
#from jwt import login_required

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/login",methods=["POST"])
def login():
     req=UserSchema().load(json.loads(request.data))
     res=Service().login(req)
     if len(res) == 0:
          return jsonify({'result':'invalid'})   
     else:
          return jsonify({'token':res})

@app.route("/register",methods=["POST"])
def register():
     req=UserSchema().load(json.loads(request.data))
     res=Service().register(req)
     array=[]
     if isinstance(res,int) == True:
          return jsonify({'result':'not found'})   
     else:
          for i in res:
               array.append(i.text)
          return jsonify({'result':array})

@app.route("/saveAcc",methods=["POST"])
def saveAcc():
     req=UserSchema().load(json.loads(request.data))
     res=Service().saveAcc(req)
     return jsonify({'result':'OK'})

@app.route("/getPubs",methods=["POST"])
def getPubs():
     req=UserSchema().load(json.loads(request.data))
     res=Service().getPubs(req)
     return jsonify({'infos':res})
     
if __name__ == '__main__':
     app.run(port=5000)