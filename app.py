from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# Route for index.html (Home Page)
@app.route('/')
def index():
    return render_template('/index.html')

# Generic route for each product request
@app.route('/google-charts/<stockname>')
def google_time_series(stockname):

    # Connecting to cloud database (MongoDb)
    client = MongoClient("mongodb+srv://mohitm12:Password1@dbcluster.x93gw.mongodb.net/StockDB?ssl=true&ssl_cert_reqs=CERT_NONE")
    db = client.get_database('StockDB')
    records = db[stockname]
    
    # Getting the latest record
    for x in records.find():
        data = x

    data = data['values']

    # Formatting data according the syntax required by Google Charts 
    custom_data = {'Datetime' : 'Closing value'}
    for x in data:
        custom_data[x['datetime']] = float(x['close'])

    # Sending request to the template 'time-series.html' along with the custom data
    return render_template('/time-series.html', data=custom_data, title=stockname)


if __name__ == "__main__":
    app.run()