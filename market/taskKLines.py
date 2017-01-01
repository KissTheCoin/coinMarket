# -*- coding:utf-8 -*-
import DB
import constant
import calKLine

calKTypes = [
    constant._K_TYPE_1MIN,
    constant._K_TYPE_5MIN,
    constant._K_TYPE_10MIN,
    constant._K_TYPE_30MIN,
    constant._K_TYPE_1HOUR,
    constant._K_TYPE_4HOUR,
    constant._K_TYPE_12HOUR,
    constant._K_TYPE_1DAY,
    constant._K_TYPE_1WEEK,
    constant._K_TYPE_1MONTH
]

lastTradeIdKey = 'calTradesLastId'

while True:
    # 获取配置中最后一次更新的交易ID
    lastTradeId = DB.configQueryByApp(lastTradeIdKey)
    tradesList = DB.queryTradesOrderById(int(lastTradeId))
    if tradesList is None or len(tradesList) <= 0:
        pass
    else:
        for trade in tradesList:
            for kType in calKTypes:
                # 计算
                kIndex = calKLine.calKLineIndexTimestamp(trade['date'], kType)
                kLine = calKLine.queryKlineOne(kType, kIndex)
                kLine = calKLine.calKline(trade, kLine)
                # 写入数据库
                DB.insertKLine(kLine)
                # 更新最后同步的ID
                DB.configUpdateByApp(lastTradeIdKey, trade['id'])
