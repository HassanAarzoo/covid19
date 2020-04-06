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
    district_data = []
    india_data = requests.get('https://api.covid19india.org/v2/state_district_wise.json').json()
    state_data = [data for data in india_data if state.lower() in data['state'].lower()]
    if state_data:
        district_data = [data for data in state_data[0]['districtData'] if district.lower() in data['district'].lower()]
    return district_data


if __name__ == '__main__':
    app.run()
