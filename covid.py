import requests
import json

from flask import Flask 
from flask import request


app = Flask(__name__)
@app.route("/")
def get_secret_message():
    return "Wassup"

@app.route("/covid")
def get_data():
    state = request.args.get('state', default='', type=str)
    district = request.args.get('district', default='', type=str)
    print(state)
    print(district)
    india_data = requests.get('https://api.covid19india.org/v2/state_district_wise.json').json()
    for state_data in india_data:
        for district_data in state_data['districtData']:
            #if 'Thrissur' in district_data['district']:
            if 'Kolhapur' in district_data['district']:
                print(district_data)
            if 'Solapur' in district_data['district']:
                print(district_data)
            if 'Satara' in district_data['district']:
                print(district_data)
            if 'Sangli' in district_data['district']:
                print(district_data)
            if 'Pune' in district_data['district']:
                print(district_data)
            #print(district_data['district'])
    return "Hello"


if __name__ == '__main__':
    app.run()
