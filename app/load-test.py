# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from pymongo import MongoClient

if __name__ == '__main__':

    names = ['InstrumentID', 'TradingDay', 'ActionDay', 'UpdateTime', 'UpdateMillisec', 'LastPrice', 'Volume',
             'HighestPrice', 'LowestPrice', 'OpenPrice', 'ClosePrice', 'AveragePrice', 'AskPrice1', 'AskVolume1',
             'BidPrice1', 'BidVolume1', 'UpperLimitPrice', 'LowerLimitPrice', 'OpenInterest', 'Turnover',
             'PreClosePrice', 'PreOpenInterest', 'PreSettlementPrice']

    df = pd.read_csv('/Volumes/Transcend/rb1805/rb1805(1.11).csv', header=0, names=names, skip_blank_lines=True,
                     delimiter=',', index_col=False)

    dict_data = df.to_dict(orient='index')

    for key in dict_data:
        bson = {"key": key, "file": "rb1805(1.11).csv", "value": dict_data[key]}
        conn = MongoClient('127.0.0.1', 27017)
        db = conn.transaction
        my_set = db.data
        my_set.insert(bson)
        print("insert: " + "key:" + key + " file: " + "rb1805(1.11).csv")
