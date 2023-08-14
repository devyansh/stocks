import json
from flask import Flask
from celery import Celery
from flask import jsonify, request
from tasks.celery_worker import process_stock_data
from tasks.celery_worker import test_method
from datetime import datetime, timedelta

app = Flask(__name__)

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0' 

celery = Celery(
    app.import_name,
    broker=app.config['CELERY_BROKER_URL'],
    backend=app.config['CELERY_RESULT_BACKEND']
)

@app.route('/')
def index():
    return 'Hello, World! This is the Flask REST API.'

@app.route('/stocks', methods=['GET'])
def get_stock_data():
    try:
        
        return handle_action(request)
    except:
        return {'Error' : 'InternalError'},500


@app.route('/stocks', methods=['POST'])
def post_stock_data():
    try:
        return handle_action(request)
    except:
        return {'Error' : 'InternalError'},500

def handle_action(request):
    stock_symbol = request.args.get('symbol')
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    if not end_date_str:
        end_date_str = start_date_str

    formatted_start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    formatted_end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    final_list = []
    while formatted_start_date <= formatted_end_date:
        stock_data_for_date = process_stock_data.delay(stock_symbol, round(formatted_start_date.timestamp()))
        normalized_data = normalize_data(formatted_start_date, stock_data_for_date, stock_symbol)
        final_list.append(normalized_data)
        formatted_start_date += timedelta(days=1)
    return final_list


def normalize_data(date, stock_data_for_date, symbol):
    return {
        'date': date.strftime("%Y/%m/%d, %H:%M:%S"),
        'close': stock_data_for_date.get()['close_price'][0],
        'open': stock_data_for_date.get()['open_price'][0], 
        'status': stock_data_for_date.get()['status'][0], 
        'symbol': symbol,
    }


