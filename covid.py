import requests
import json

from collections import defaultdict
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
    state_data = [data for data in india_data if state.lower() in data['state'].lower()]
    district_data = [data for data in state_data[0]['districtData'] if district.lower() in data['district'].lower()]
    if district_data:
        return district_data[0]
    # TODO Might be a good idea to send the name of states and district
    return {"message": "Could not find data "}


if __name__ == '__main__':
    app.run()
