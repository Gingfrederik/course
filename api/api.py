import json
from flask_cors import CORS
from flask import Flask,jsonify,request,Response
from pymongo import MongoClient

uri = "mongodb://api:api1234@ds139362.mlab.com:39362/course_list"
client = MongoClient(uri)
db = client['course_list']
collect = db['courses']


app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route("/course_list",methods=['GET'])
def course_list():
    data = []
    dic = {}
    try:
        for x in request.args:
            print(x)
            dic[x] = request.args.get(x)
        for x in collect.find(dic):
            del x['_id']
            data.append(x)
        return json.dumps(data, ensure_ascii=False)
    except:
        pass

if __name__ == "__main__":
    app.run()
