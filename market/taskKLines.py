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
    tradesList = DB.queryTradesOrderById(int(lastTradeId), 1000)
    if tradesList is None or len(tradesList) <= 0:
        pass
    else:
        kLineObjList = {}
        lastTradeId = None
        for trade in tradesList:
            for kType in calKTypes:
                # 计算
                kIndex = calKLine.calKLineIndexTimestamp(trade['date'], kType)
                kLine = calKLine.queryKlineOne(kType, kIndex)
                kLine = calKLine.calKline(trade, kLine)
                kLineObjList[str(kType) + "-" + str(kIndex)] = kLine
                lastTradeId = trade['id']

        for key in kLineObjList:
            # 写入数据库
            DB.insertKLine(kLineObjList[key])
        # 更新最后同步的ID
        if lastTradeId is not None:
            DB.configUpdateByApp(lastTradeIdKey, lastTradeId)
