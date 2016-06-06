#!usr/bin/python
# Filename: storage_pool_txt2json.py
import json


def main():
    stock_dict = {}
    txt_path = r"D:\code\Projects\stockData\stockData\stockPool.txt"

    with open(txt_path, 'r') as txt_file:
        for line in txt_file:
            temp = line.split(',')
            stock_dict[temp[0]] = ''
    with open('stock_pool.json', 'w') as json_file:
        json.dump(stock_dict, json_file, indent=2, sort_keys=True, separators=(',', ':'))

if __name__ == "__main__":
    main()
# End of storage_pool_txt2json.py
