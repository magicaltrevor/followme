-- MySQL dump 10.11
--
-- Host: localhost    Database: followme
-- ------------------------------------------------------
-- Server version	5.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_to_monitors`
--

DROP TABLE IF EXISTS `accounts_to_monitors`;
CREATE TABLE `accounts_to_monitors` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  `min_tweets` int(11) default NULL,
  `min_followers` int(11) default NULL,
  `min_friends` int(11) default NULL,
  `search_term` varchar(255) default NULL,
  `ratio` int(11) default NULL,
  `max_ratio` int(11) default NULL,
  `max_follows_per_hour` int(11) default NULL,
  `number_of_days_to_follow_back` int(11) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `accounts_to_monitors`
--

LOCK TABLES `accounts_to_monitors` WRITE;
/*!40000 ALTER TABLE `accounts_to_monitors` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_to_monitors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `follow_queues`
--

DROP TABLE IF EXISTS `follow_queues`;
CREATE TABLE `follow_queues` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `accounts_to_monitor_id` int(11) default NULL,
  `followed_date` datetime default NULL,
  `rejected` int(11) default NULL,
  `followers` int(11) default NULL,
  `friends` int(11) default NULL,
  `tweets` int(11) default NULL,
  `followed_back_date` datetime default NULL,
  `unfollowed` int(11) default NULL,
  `twitter_id` int(11) default NULL,
  PRIMARY KEY  (`id`),
  KEY `accounts_to_monitor_id` (`accounts_to_monitor_id`),
  KEY `followed_date` (`followed_date`),
  KEY `rejected_accounts_to_monitor_id` (`rejected`,`accounts_to_monitor_id`),
  KEY `rejected` (`rejected`),
  KEY `username_accounts_to_monitor_id` (`username`,`accounts_to_monitor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `follow_queues`
--

LOCK TABLES `follow_queues` WRITE;
/*!40000 ALTER TABLE `follow_queues` DISABLE KEYS */;
/*!40000 ALTER TABLE `follow_queues` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2009-03-10 18:57:13
