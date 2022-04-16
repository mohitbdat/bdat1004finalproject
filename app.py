from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/google-charts/<stockname>')
def google_time_series(stockname):

    client = MongoClient("mongodb+srv://mohitm12:Password1@dbcluster.x93gw.mongodb.net/StockDB?ssl=true&ssl_cert_reqs=CERT_NONE")
    db = client.get_database('StockDB')
    records = db[stockname]
    
    for x in records.find():
        data = x

    #data = records.find().sort("_id", -1)
    data = data['values']

    custom_data = {'Datetime' : 'Closing value'}

    for x in data:
        custom_data[x['datetime']] = float(x['close'])

    return render_template('/time-series.html', data=custom_data, title=stockname)


if __name__ == "__main__":
    app.run()