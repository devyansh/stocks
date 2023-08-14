import requests
from celery import Celery
# from app import app

app = Celery(
    'celery_worker',
    # broker='redis://redis:6379/0',  # Use the service name as the hostname
    broker = 'redis://localhost:6379/0'
    # backend='redis://redis:6379/0'
)

FINNHUB_API_KEY = 'cjbbmfpr01qn9c1l9ge0cjbbmfpr01qn9c1l9geg'

@app.task
def process_stock_data(stock_symbol, start_date, end_date):
    print('ENETERED PROCESS STOCK')
    url = f"https://finnhub.io/api/v1/stock/candle?symbol={stock_symbol}&resolution=D&from={start_date}&to={end_date}&token={FINNHUB_API_KEY}"
    
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        open_prices = data.get('o')
        close_prices = data.get('c')
        processed_data = {'open_prices': open_prices, 'close_prices': close_prices}
        print('HEEEEEEEEEEEEELOOOOOOOOOOOOOOOOOOOOOO')
        print(processed_data)
        return processed_data
    else:
        print('ELSSSSSSSSSSSSSSEREEEEEEEEEEEEE')
        return None
