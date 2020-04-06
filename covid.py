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

    india_data = requests.get('https://api.covid19india.org/v2/state_district_wise.json').json()
    for state_data in india_data:
        if state.lower() in state_data['state'].lower():
            for district_data in state_data['districtData']:
                if district.lower() in district_data['district'].lower():
                    return district_data
    return {}


if __name__ == '__main__':
    app.run()
