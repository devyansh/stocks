# from app import app
from app import app
# from flask import jsonify, request
# from tasks.celery_worker import process_stock_data
# from tasks import celery_worker

@app.route('/')
def index():
    return 'Hello, World! This is the Flask REST API.'

# @app.route('/get_stock_data', methods=['GET'])
# def get_stock_data():
#     stock_symbol = request.args.get('symbol')
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')

#     # Replace this with your Celery task call to fetch stock data
#     result = process_stock_data.apply_async(args=[stock_symbol, start_date, end_date])

#     result = {
#         'symbol': stock_symbol,
#         'start_date': start_date,
#         'end_date': end_date,
#         'data': []  # Placeholder for fetched data
#     }

#     return jsonify(result)
