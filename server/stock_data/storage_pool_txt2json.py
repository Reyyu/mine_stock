#!usr/bin/python
# Filename: storage_pool_txt2json.py
import json


def main():
    txt_path = r"D:\code\Projects\stockData\stockData\stockPool.txt"
    txt_file = open(txt_path, 'r')
    stock_dict = { }
    for line in txt_file:
        temp = line.split(',')
        stock_dict[temp[0]] = ''
    else:
        txt_file.close()

    encode_string = json.dumps(stock_dict, indent=2, sort_keys=True, separators=(',', ':'))

    json_file = open('stock_pool.json', 'w')
    json_file.write(encode_string)
    json_file.close()

if __name__ == "__main__":
    main()

# End of storage_pool_txt2json.py
