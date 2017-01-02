
CREATE TABLE `market_trades` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `market` tinyint(2) unsigned NOT NULL COMMENT '交易市场',
  `coin` tinyint(2) unsigned NOT NULL COMMENT '火币类型',
  `date` int(11) unsigned NOT NULL COMMENT '交易时间',
  `amount` decimal(15,6) unsigned NOT NULL COMMENT '成交数量',
  `price` decimal(10,3) unsigned NOT NULL COMMENT '成交价格',
  `type` tinyint(1) unsigned NOT NULL COMMENT '成交方向 1 买 2 卖',
  `tid` bigint(20) unsigned NOT NULL COMMENT '关联id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `config` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `app` varchar(20) NOT NULL DEFAULT '' COMMENT '程序项',
  `val` varchar(100) NOT NULL DEFAULT '' COMMENT '程序值',
  PRIMARY KEY (`id`),
  KEY `idx_app` (`app`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `config` (app, val) VALUES ('calTradesLastId', '0');

CREATE TABLE `market_kline` (
  `k_type` smallint(5) unsigned NOT NULL COMMENT 'K线类型',
  `k_index` int(11) unsigned NOT NULL COMMENT 'K线索引',
  `high` decimal(10,3) unsigned NOT NULL COMMENT '最高价',
  `low` decimal(10,3) unsigned NOT NULL COMMENT '最低价',
  `open` decimal(10,3) unsigned NOT NULL COMMENT '开盘价',
  `close` decimal(10,3) unsigned NOT NULL COMMENT '收盘价',
  `volume` decimal(15,6) unsigned NOT NULL COMMENT '成家量',
  `date` int(11) unsigned NOT NULL COMMENT '时间',
  UNIQUE KEY `idx_type_index` (`k_type`,`k_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;