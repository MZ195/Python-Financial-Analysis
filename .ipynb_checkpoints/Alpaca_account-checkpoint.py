import configparser
import requests
import json

class Alpaca_account():
    def __init__(self, config_file_path):
        config = configparser.ConfigParser()
        config.read(config_file_path)

        self.API_KEY = config['KEYS']['API_KEY']
        self.SECRECT_KEY = config['KEYS']['SECRET_KEY']
        self.BASE_URL = config['URL']['BASE']
        self.DATA_URL = config['URL']['DATA']
        
        base_url = config['URL']['BASE']
        api_key = config['KEYS']['API_KEY']
        secret_key = config['KEYS']['SECRET_KEY']
        
        self.ACCOUNT_URL = f"{base_url}/v2/account"
        self.ORDERS_URL = f"{base_url}/v2/orders"
        
        self.HEADERS = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": secret_key}
        
    def get_account(self):
        """
        Gets the accoutn's data
        """
        
        res = requests.get(self.ACCOUNT_URL, headers= self.HEADERS)
        return json.loads(res.content)
    
    def get_orders(self):
        """
        Gets the previous orders placed by the account
        """
        
        res = requests.get(self.ORDERS_URL, headers= self.HEADERS)
        return json.loads(res.content)
    
    def create_order(self, symbol, qty, side, order_type, time_in_force):
        """
        Create a POST request to either buy or sell
        """
        
        data = {
            'symbol': symbol,               # Company name code
            'qty': qty,                     # Quantity of equities to buy/sell
            'side': side,                   # Type of action (Buy/Sell)
            'type': order_type,              # Type of order
            'time_in_force': time_in_force  # When will the order be executed
        }
        
        res = requests.post(self.ORDERS_URL, json= data, headers= self.HEADERS)
        return json.loads(res.content)
    
    def create_order_limit(self, symbol, qty, side, order_type, time_in_force, limit_price):
        """
        Create a POST request to either buy or sell
        """
        
        data = {
            'symbol': symbol,               # Company name code
            'qty': qty,                     # Quantity of equities to buy/sell
            'side': side,                   # Type of action (Buy/Sell)
            'type': order_type,              # Type of order
            'time_in_force': time_in_force, # When will the order be executed
            'limit_price': limit_price      # The price limit
        }
        
        res = requests.post(self.ORDERS_URL, json= data, headers= self.HEADERS)
        return json.loads(res.content)
    
    def create_order_complete(self, symbol, qty, side, order_type, time_in_force, limit_price, stop_loss):
        """
        Create a POST request to either buy or sell
        """
        
        data = {
            'symbol': symbol,               # Company name code
            'qty': qty,                     # Quantity of equities to buy/sell
            'side': side,                   # Type of action (Buy/Sell)
            'type': order_type,             # Type of order
            'time_in_force': time_in_force, # When will the order be executed
            'order_class': 'bracket',       # Bracket orders allow us to dynamically sell or buy based on our limits
            'take_profit': {'limit_price': limit_price},
            'stop_loss': {'stop_price': stop_loss}
        }
        
        res = requests.post(self.ORDERS_URL, json= data, headers= self.HEADERS)
        return json.loads(res.content)
    
    def get_bars_data(self, period, symbol, limit):
        url = f"{self.DATA_URL}/bars/{period}?symbols={symbol}&limit={limit}"
        res = requests.get(url, headers = self.HEADERS)
        
        return json.loads(res.content)