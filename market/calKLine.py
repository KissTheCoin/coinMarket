# -*- coding:utf-8 -*-

from datetime import *
import DB


# 根据时间戳，返回指定K线类型的索引
def calKLineIndexTimestamp(nowTimestamp, kType):
    kSecond = kType * 60
    return nowTimestamp - (nowTimestamp % kSecond)


# 查询指定类型与索引的K线数据
def queryKlineOne(kType, kIndex):
    kLine = DB.queryKLineOne(kType, kIndex)
    kLineObj = {
        'kType': kType,
        'kIndex': kIndex,
        'high': None,
        'low': None,
        'open': None,
        'close': None,
        'volume': 0,
        'date': kIndex,
    }
    if None is kLine:
        return kLineObj
    kLineObj['high'] = kLine[2]
    kLineObj['low'] = kLine[3]
    kLineObj['open'] = kLine[4]
    kLineObj['close'] = kLine[5]
    kLineObj['volume'] = kLine[6]
    kLineObj['date'] = kLine[7]
    return kLineObj


# 根据成交信息与K线数据，计算新的K线
def calKline(trade, kLine):
    kLine['high'] = trade['price'] if kLine['high'] is None else \
        trade['price'] if trade['price'] > kLine['high'] else kLine['high']
    kLine['low'] = trade['price'] if kLine['low'] is None else \
        trade['price'] if trade['price'] < kLine['low'] else kLine['low']
    kLine['open'] = trade['price'] if kLine['open'] is None else kLine['open']
    kLine['close'] = trade['price']
    kLine['volume'] += trade['amount']
    return kLine
