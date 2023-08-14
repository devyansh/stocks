import json
from flask import Flask
from celery import Celery
from flask import jsonify, request
from tasks.celery_worker import process_stock_data

app = Flask(__name__)

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # Replace with Redis host
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'  # Replace with Redis host

celery = Celery(
    app.import_name,
    broker=app.config['CELERY_BROKER_URL'],
    backend=app.config['CELERY_RESULT_BACKEND']
)

@app.route('/')
def index():
    return 'Hello, World! This is the Flask REST API.'

@app.route('/get_stock_data', methods=['GET'])
def get_stock_data():
    stock_symbol = request.args.get('symbol')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Replace this with your Celery task call to fetch stock data
    print('JUST BEFORE PROCESS STOCK')
    result = process_stock_data(stock_symbol, start_date, end_date)
    print('YEEEEEEELLLO')
    print(result)
    print(type(result))

    final_result = {
        'symbol': stock_symbol,
        'start_date': start_date,
        'end_date': end_date,
        'open': result.get('open_prices')[0],
        'close': result.get('close_prices')[0]
    }

    return jsonify(final_result)
