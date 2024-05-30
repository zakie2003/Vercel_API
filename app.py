from flask import Flask,request,jsonify
from model import *
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route("/",methods=('GET', 'POST'))
def inp():   
    if request.method=="POST":
            req_json=request.json
            inpf={"venue":req_json["venue"],"innings":req_json["inning"],"batting_team":req_json["bat"],"bowling_team":req_json["bowl"],"batsmen":req_json["wic"],"bowlers":req_json["numbboler"]}
            inpf=pd.DataFrame.from_dict([inpf])
            # preds=pd.read_csv("test_file.csv")
            print(inpf)
            aaa=MyModel()
            zzz=aaa.predict(inpf)
            response= jsonify({"prediction": zzz[0][0]})
            return  response

    return jsonify({"prediction":0}) 
           

# app.run(host='0.0.0.0',debug=True)       
