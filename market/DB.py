# -*- coding: utf-8 -*-
import MySQLdb
import config
import logging

dbconn = MySQLdb.connect(
    host=config._DB['host'],
    port=config._DB['port'],
    user=config._DB['user'],
    passwd=config._DB['pwd'],
    db=config._DB['dbname'],
)


def queryLastTid(market, coin):
    """
    查询数据库最后一笔更新的TID
    :param market:
    :param coin:
    :return:
    """
    try:
        cursor = dbconn.cursor()
        sql = 'SELECT tid FROM market_trades WHERE market = %d AND coin = %d ORDER BY tid DESC LIMIT 1' % (market, coin)
        cursor.execute(sql)
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return 1
    except:
        logging.error('数据库出错')
        dbconn.rollback()


def insertTrades(tradesList):
    if len(tradesList) <= 0:
        return
    for trade in tradesList:
        sql = """
        INSERT INTO market_trades (market, coin, `date`, amount, price, `type`, tid)
        VALUE (%d, %d, %d, %.6f, %.3f, %d, %d)
        """ % (
            trade['market'], trade['coin'], trade['date'], trade['amount'], trade['price'], trade['type'], trade['tid'])
        try:
            cursor = dbconn.cursor()
            cursor.execute(sql)
            dbconn.commit()
        except:
            logging.error('数据库错误，执行插入成交记录的过程中...')
            dbconn.rollback()
            return
