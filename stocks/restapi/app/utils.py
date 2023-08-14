def normalize_stock_data(data):
    open_prices = data.get('open_prices', [])
    close_prices = data.get('close_prices', [])
    
    normalized_data = []
    for open_price, close_price in zip(open_prices, close_prices):
        normalized_entry = {
            'open_price': open_price,
            'close_price': close_price
        }
        normalized_data.append(normalized_entry)
    
    return normalized_data
