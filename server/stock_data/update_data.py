#!usr/bin/python
# Filename: update_data.py
import json
import urllib.request


def update_stock_info():
    stock_pool_path = r'../public/config/stock_pool.json'
    with open(stock_pool_path, 'r') as stock_pool_file:
        stock_pool = json.load(stock_pool_file)
        # print(data)

try:
    url = ""
    with urllib.request.urlopen(r'') as response:
        stock_data = response.read().decode('utf-8')
Exception:


def main():
    update_stock_info()

if __name__ == "__main__":
    main()

# End of update_data.py
