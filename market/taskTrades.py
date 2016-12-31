# -*- coding:utf-8 -*-

import DB
import captureTrades
import constant


def huobiTrades():
    market = constant.EXCHANGE['huobi']
    coin = constant._BTC
    lastTid = DB.queryLastTid(market, coin)
    if lastTid:
        tradesList = captureTrades.getHuobiTrades(coin, lastTid)
        DB.insertTrades(tradesList)


def okcoinTrades():
    market = constant.EXCHANGE['okcoin']
    coin = constant._BTC
    lastTid = DB.queryLastTid(market, coin)
    if lastTid:
        tradesList = captureTrades.getOkcoinTrades(coin, lastTid)
        DB.insertTrades(tradesList)


huobiTrades()
okcoinTrades()
