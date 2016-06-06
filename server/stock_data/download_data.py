#!usr/bin/env python3
# -*- coding:utf-8 -*-


def download_history_data_from_yahoo(url):
    """从雅虎网站下载历史数据

    Args:
        url: 获取数据的URL

    Returns:
        none

    Raises:
        none
    """

    try:
        with urllib.request.urlopen(url) as response:
            stock_data = response.read().decode("utf-8")
            return stock_data
    except urllib.error.URLError:
        print("urllib.error.URLError: {0}".format(url))
    except urllib.error.HTTPError as http_error:
        print("HTTPError: {0}".format(http_error.reason))


def download_history_data_from_yahoo(code, url, force_update=False):
    """从雅虎网站下载历史数据

    Args:
        code: 股票代码
        url: 获取数据的URL
        force_update: 是否强制重新下载所有数据，False：比较更新，True：强制全部更新

    Returns:
        none

    Raises:
        none
    """

    # 如果是比较更新，则先读取原有的数据，查找哪些数据不存在
    if not force_update:
        with open("history_data/{0}".format(code))  as old_file:
            pass

    try:
        with urllib.request.urlopen(url) as response:
            stock_data = response.read().decode("utf-8")
            print(stock_data)
    except urllib.error.URLError:
        print("urllib.error.URLError: {0}".format(url))
    except urllib.error.HTTPError as http_error:
        print("HTTPError: {0}".format(http_error.reason))


def main():
    # 解析命令行参数
    arg_parser = argparse.ArgumentParser(description="Download history stock data from yahoo")
    arg_parser.add_argument("-c", "--code", required=True, help="Code of stock")
    arg_parser.add_argument("-d", "--day", type=int, required=True, help="Count of days")

    args = arg_parser.parse_args()
    # print(args)

    if len(args.code) != 6 or args.day <= 0 or args.day >= 9999:
        print("input error")
    else:
        download_history_data_from_yahoo(args.code, args.day)


if __name__ == "__main__":
    main()