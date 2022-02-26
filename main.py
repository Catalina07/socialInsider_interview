from flask import Flask,jsonify,render_template,request
import requests

app = Flask(__name__)

@app.route("/getDataProfile",methods=["POST","GET"])
def getDataProfile():
    if request.method=="GET":
        id_get_profile=request.args.get("id")
        facebook_page=request.args.get("profile_type")
        date1=request.args.get("date1")
        date2=request.args.get("date2")
        timezone=request.args.get("timezone")
    print(id_get_profile,facebook_page,date1,date2,timezone)
    data = get_profile_data(id_get_profile,facebook_page,date1,date2,timezone)
    return jsonify(data)

@app.route("/getBrands",methods=["POST","GET"])
def getBrands():
    data = get_brands()
    return jsonify(data)

@app.route("/",methods=["POST","GET"])
def index():
    return render_template("index.html")


def get_profile_data(id_get_profile,facebook_page,date1,date2,timezone):
    endpoint="https://app.socialinsider.io/api"
    data = {
        "id" : 1,
        "method" : "socialinsider_api.get_profile_data",
        "params":{
            "id":id_get_profile,
            "profile_type": facebook_page,
            "date": {
                "start": date1,
                "end": date2,
                "timezone": timezone
            }
        }
    }
    headers = {"Authorization": "Bearer API_KEY_TEST"}
    r=requests.post(endpoint, json=data, headers=headers)
    return r.json()

def get_brands():
    endpoint="https://app.socialinsider.io/api"
    data = {
        "jsonrpc": "2.0", 
        "id": 0,
        "method": "socialinsider_api.get_brands", 
        "params": {
            "projectname": "API_test"
        }
    }
    headers = {"Authorization": "Bearer API_KEY_TEST"}
    r=requests.post(endpoint, json=data, headers=headers)
    return r.json()



if __name__=='__main__':
    app.run()