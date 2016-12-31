# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.12)
# Database: coin_market
# Generation Time: 2016-12-31 10:12:12 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table market_trades
# ------------------------------------------------------------

DROP TABLE IF EXISTS `market_trades`;

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




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
