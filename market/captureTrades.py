# -*- coding: utf-8 -*-
import urllib2
import json
import constant


def getHuobiTrades(coin, lastTid):
    """
    获取火币网最后一次成交id后的成交记录
    :param coin: 币种
    :param lastTid: 最后一次获取的id
    :return: array
    """
    url = constant._HUOBI_TRADES_URL[coin]
    url = url % lastTid
    urlObj = urllib2.urlopen(url)
    jsonStr = urlObj.read()
    jsonObj = json.loads(jsonStr)
    resArr = []
    for j in jsonObj:
        res = {
            'market': constant.EXCHANGE['huobi'],
            'coin': coin,
            'date': j['date'],
            'amount': j['amount'],
            'price': j['price'],
            'type': constant._BUY if j['type'] == 'buy' else constant._SELL,
            'tid': j['tid'],
        }
        resArr.append(res)
    return resArr


def getOkcoinTrades(coin, lastTid):
    """
    获取OKcoin最后一次成交id后的成交记录
    :param coin: 币种信息
    :param lastTid: 最后一次成交id
    :return: array
    """
    url = constant._OKCOIN_TRADES_URL[coin]
    url = url % lastTid
    urlObj = urllib2.urlopen(url)
    jsonStr = urlObj.read()
    jsonObj = json.loads(jsonStr)
    resArr = []
    for j in jsonObj:
        res = {
            'market': constant.EXCHANGE['okcoin'],
            'coin': coin,
            'date': j['date'],
            'amount': float(j['amount']),
            'price': float(j['price']),
            'type': constant._BUY if j['type'] == 'buy' else constant._SELL,
            'tid': j['tid'],
        }
        resArr.append(res)
    return resArr
