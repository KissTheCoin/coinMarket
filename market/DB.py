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
    """
    插入一笔成交记录
    :param tradesList:
    :return:
    """
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


def queryTradesOrderById(id, limit):
    """
    查询大于这个ID成交记录
    :param id:
    :return:
    """
    # TODO 只支持火币BTC的
    sql = 'SELECT id, price, amount, `date` FROM market_trades ' \
          'WHERE id > %d AND market = 1 AND coin = 1 ORDER BY id ASC LIMIT %d' % (id, limit)
    cursor = dbconn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    if res is None:
        return None
    tradeArr = []
    for r in res:
        trade = {
            'id': r[0],
            'price': r[1],
            'amount': r[2],
            'date': r[3]
        }
        tradeArr.append(trade)
    return tradeArr


def queryKLineOne(kType, kIndex):
    """
    查询指定K线类型与索引的K线数据
    :param kType:
    :param kIndex:
    :return:
    """
    sql = 'SELECT * FROM market_kline WHERE k_type = %d AND k_index = %d LIMIT 1' % (kType, kIndex)
    try:
        cursor = dbconn.cursor()
        cursor.execute(sql)
        res = cursor.fetchone()
        return res
    except:
        logging.error('数据库出错，查询k线数据出错')
        dbconn.rollback()


def insertKLine(kLine):
    """
    插入一条K线数组
    :param kLine:
    :return:
    """
    sql = """
    REPLACE INTO market_kline (k_type, k_index, high, low, `open`, `close`, volume, `date`)
    VALUES (%d, %d, %.3f, %.3f, %.3f, %.3f, %.6f, %d)
    """ % (kLine['kType'], kLine['kIndex'], kLine['high'], kLine['low'],
           kLine['open'], kLine['close'], kLine['volume'], kLine['date'])
    try:
        cursor = dbconn.cursor()
        cursor.execute(sql)
        dbconn.commit()
    except:
        logging.error('数据库错误，执行插入KLine记录的过程中...')
        dbconn.rollback()


def configQueryByApp(app):
    """
    查询指定的配置项值
    :param app:
    :return:
    """
    sql = "SELECT val FROM config WHERE app = '%s' LIMIT 1" % (app)
    cursor = dbconn.cursor()
    cursor.execute(sql)
    return cursor.fetchone()[0]


def configUpdateByApp(app, val):
    """
    更新指定的配置项
    :param app:
    :param val:
    :return:
    """
    sql = "UPDATE config SET val = '%s' WHERE app = '%s'" % (val, app)
    cursor = dbconn.cursor()
    cursor.execute(sql)
    dbconn.commit()
