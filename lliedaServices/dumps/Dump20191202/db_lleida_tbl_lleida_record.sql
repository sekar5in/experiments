-- MySQL dump 10.17  Distrib 10.3.11-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: db_lleida
-- ------------------------------------------------------
-- Server version	10.3.11-MariaDB

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
-- Table structure for table `tbl_lleida_record`
--

DROP TABLE IF EXISTS `tbl_lleida_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_lleida_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tbl_lleida_record_eventid` varchar(255) NOT NULL,
  `tbl_lleida_record_from` varchar(255) NOT NULL,
  `tbl_lleida_record_subj` varchar(255) NOT NULL,
  `tbl_lleida_record_mail_id` varchar(255) NOT NULL,
  `tbl_lleida_record_msg_id` varchar(255) NOT NULL,
  `tbl_lleida_record_rcode` varchar(255) NOT NULL,
  `tbl_lleida_record_reason` varchar(255) NOT NULL,
  `is_cert_processed` tinyint(1) DEFAULT NULL,
  `is_addendum_processed` tinyint(1) DEFAULT NULL,
  `tbl_lleida_record_order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`is_cert_processed` in (0,1)),
  CONSTRAINT `CONSTRAINT_2` CHECK (`is_addendum_processed` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_lleida_record`
--

LOCK TABLES `tbl_lleida_record` WRITE;
/*!40000 ALTER TABLE `tbl_lleida_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_lleida_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-02 17:39:35
