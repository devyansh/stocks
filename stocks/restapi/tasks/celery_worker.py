import requests
# from celery import Celery
from celeryconfig import app
# from app import app

FINNHUB_API_KEY = 'cjbbmfpr01qn9c1l9ge0cjbbmfpr01qn9c1l9geg'
print('CELERY WORKER FILE')

@app.task
def process_stock_data(stock_symbol, date):
    print('PROCESS STOCK DATA CALLED')
    url = f"https://finnhub.io/api/v1/stock/candle?symbol={stock_symbol}&resolution=D&from={date}&to={date}&token={FINNHUB_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('s', '') != 'no_data':
            print(data)
            processed_data = {'open_price': data.get('o'), 'close_price': data.get('c'), 'status': data.get('s')}
        else:
            processed_data = {'open_price': [None], 'close_price': [None], 'status': data.get('s')}
    else:
        processed_data = {'open_price': [None], 'close_price': [None], 'status': 'ERROR'}
    print('PROCESSED DATA')
    print(processed_data)
    return processed_data

@app.task
def test_method(stock_symbol):
    final_string = stock_symbol
    return final_string