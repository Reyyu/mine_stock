#!usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import argparse
import datetime


def code_suffix(code):
    """按照股票代码得到股票代码后缀

    Args:
        code: 股票代码

    Returns:
        股票代码后缀

    Raises:
        None
    """

    if not code.strip():
        return ""

    if code[0] == "3" or code[0] == "0":
        return "sz"
    elif code[0] == "6":
        return "ss"
    else:
        return ""


def compose_yahoo_history_data_url_with_date(code, date_begin, date_end=datetime.date.today()):
    """合成获取雅虎股票数据的URL：指定的开始日期到指定的结束日期

    Args:
        code: 股票代码
        date_begin: 开始日期
        date_end: 结束日期

    Returns:
        合成的URL字符串
        example:

        股票000001从20130905至今的数据
        http://table.finance.yahoo.com/table.csv?s=000001.sz&g=d&a=8&b=20&c=2015&ignore=.csv

        IBM股票从1991年10月16日起到2013年9月5日的数据
        http://table.finance.yahoo.com/table.csv?s=ibm&d=8&e=5&f=2013&g=d&a=9&b=16&c=1991&ignore=.csv

    Raises:
        None
    """

    suffix = code_suffix(code)
    if len(code) <= 0 or len(code) > 6 or not suffix:
        print("compose_yahoo_history_data_url error: code={0}".format(code))
        return ""
    else:
        return "http://table.finance.yahoo.com/table.csv?s={0}.{1}&d={2}&e={3}&f={4}&g=d&a={5}" \
               "&b={6}&c={7}&ignore=.csv".format(code, suffix, date_end.month-1, date_end.day, date_end.year,
                                                 date_begin.month-1, date_begin.day, date_begin.year)


def compose_yahoo_history_data_url_with_days(code, day):
    """合成获取雅虎股票数据的URL：指定到今天为止的天数

    Args:
        code: 股票代码
        day: 需要下载的数据天数

    Returns:
        合成的URL字符串

    Raises:
        None
    """
    datetime_start = datetime.datetime.now() + datetime.timedelta(days=-day)
    return  compose_yahoo_history_data_url_with_date(code, datetime_start)


def main():
    url_1 = compose_yahoo_history_data_url_with_date("000001", datetime.date(2016, 6, 2))
    url_2 = compose_yahoo_history_data_url_with_days("000001", 60)
    print("url: ", url_1)
    print("url: ", url_2)

if __name__ == "__main__":
    main()

# End
