# -*- coding:utf-8 -*-

# 币种类型定义
_BTC = 1
_LTC = 2

# 交易类型定义
_BUY = 1
_SELL = 2

# 交易所定义
EXCHANGE = {
    'huobi' : 1,
    'okcoin' : 2
}

# 交易历史获取url地址
_HUOBI_TRADES_URL = {
    _BTC: 'https://api.huobi.com/staticmarket/trades_btc_histroy.json?since=%s',
    _LTC: 'https://api.huobi.com/staticmarket/trades_ltc_histroy.json?since=%s'
}

_OKCOIN_TRADES_URL = {
    _BTC : 'https://www.okcoin.cn/api/v1/trades.do?symbol=btc_cny&since=%s',
    _LTC : 'https://www.okcoin.cn/api/v1/trades.do?symbol=ltc_cny&since=%s'
}

_K_TYPE_1MIN = 1
_K_TYPE_5MIN = 5
_K_TYPE_10MIN = 10
_K_TYPE_30MIN = 30
_K_TYPE_1HOUR = 60
_K_TYPE_4HOUR = 240
_K_TYPE_12HOUR = 720
_K_TYPE_1DAY = 1440
_K_TYPE_1WEEK = 10080
_K_TYPE_1MONTH = 43200