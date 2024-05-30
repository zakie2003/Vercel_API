from flask import Flask,request,jsonify
from model import *


app=Flask(__name__)
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
            response.headers.add('Access-Control-Allow-Origin', '*')
            return  response
    return jsonify({"prediction":0}) 
           

if(__name__=="__main__"):
    app.run(debug=True)   
