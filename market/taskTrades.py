# -*- coding:utf-8 -*-

import DB
import captureTrades
import time
import constant
import logging


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


while True:
    try:
        huobiTrades()
    except:
        logging.error('执行火币交易抓取失败')
        time.sleep(10)
    try:
        okcoinTrades()
    except:
        logging.error('执行OK交易抓取失败')
        time.sleep(10)
    time.sleep(1)
