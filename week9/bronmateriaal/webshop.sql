-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: webshop
-- ------------------------------------------------------
-- Server version	5.7.21

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
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `﻿referentie` int(11) DEFAULT NULL,
  `naam` text,
  `omschrijving` text,
  `samenstelling` text,
  `kleur` text,
  `maat` text,
  `prijs` text,
  `foto` text,
  `categorie` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (3302182,'Wit t-shirt Ciao Bella','Wit t-shirt met gouden print Ciao Bella. Met ronde hals en korte mouwen afgewerkt met volant. ','100% katoen','Wit','92, 98, 104, 110, 116, 122, 128','7,99','assets/images/3302182.jpg','T-shirt'),(3312032,'Blauwe cold shoulder top','100% katoen','100% katoen','Blauw','92, 98, 104, 110, 116, 122, 128','7,99','assets/images/3312032.jpg','T-shirt'),(3414052,'Kobaltblauwe jurk volant','Kobaltblauwe jurk met volant en lint','100% katoen','Blauw','92, 98, 104, 110, 116, 122, 128','15','assets/images/3414052.jpg','Jurk'),(4302112,'Witte t-shirt ijsje','Witte t-shirt met ijsje in tulle. Met ronde hals en korte mouwen. ','100% katoen','Wit','92, 98, 104, 110, 116, 122, 128','12,99','assets/images/4302112.jpg','T-shirt'),(4302132,'Wit t-shirt flamingo','Wit t-shirt met print roze flamingo en pailletten. Met ronde hals en korte mouwen. ','95% katoen + 5% elasthaan','Wit','92, 98, 104, 110, 116, 122, 128','7,99','assets/images/4302132.jpg','T-shirt'),(4302142,'Wit t-shirt hartjes','Wit t-shirt met print gekleurde hartjes. Met ronde hals en korte mouwen.','95% katoen + 5% elasthaan','Wit','92, 98, 104, 110, 116, 122, 128','7,99','assets/images/4302142.jpg','T-shirt'),(4302162,'Ecru T-shirt','Ecru T-shirt met korte mouwen, glitterprint en goudkleurige strik. ','95% katoen + 5% elastaan','Ecru','92, 98, 104, 110, 116, 122, 128','9,99','assets/images/4302162.jpg','T-shirt'),(4303102,'Wit t-shirt cactus','Wit t-shirt met print cactus. Met ronde hals en korte mouwen. ','95% katoen + 5% elasthaan','Wit','92, 98, 104, 110, 116, 122, 128','7,99','assets/images/4303102.jpg','T-shirt'),(4312022,'Wit t-shirt unicorn','Wit t-shirt met print roze unicorn. Met ronde hals en korte mouwen met volant.','95% katoen + 5% elasthaan','Wit','92, 98, 104, 110, 116, 122, 128','7,99','assets/images/4312022.jpg','T-shirt'),(4413032,'Jurk met print roze en groen','Jurk met allover print flamingo en cactus in roze en groen. Versierd met flochen en zonder mouwen.','100% viscose','Multi','92, 98, 104, 110, 116, 122, 128','19,99','assets/images/4413032.jpg','Jurk'),(4413042,'Multi-gekleurde jurk strik','Gestreepte jurk in verschillende kleuren. Met fijne bretellen en strik op de rug. ','','Multi','92, 98, 104, 110, 116, 122, 128','14,00','assets/images/4413042.jpg','Jurk'),(4414012,'Roze jurk hart','Roze jurk met print hart en elastiek in de taille. Met ronde hals en korte mouwen.','100% katoen','Roze','92, 98, 104, 110, 116, 122, 128','12','assets/images/4414012.jpg','Jurk'),(4414022,'Blauwe jurk volant','Blauwe jurk met volant en kant.','100% katoen','Blauw','92, 98, 104, 110, 116, 122, 128','12','assets/images/4414022.jpg','Jurk'),(4414032,'Jurk grijs melé cactus','Jurk in grijs melé met allover cactusprint. Met ronde hals en korte mouwen.','93% katoen + 7% polyester','Grijs','92, 98, 104, 110, 116, 122, 128','12','assets/images/4414032.jpg','Jurk'),(4414042,'Gestreepte jurk Summer','Gestreepte jurk in wit en marineblauw met print Summer. Met ronde hals en korte mouwen.','100% katoen','Multi','92, 98, 104, 110, 116, 122, 128','12','assets/images/4414042.jpg','Jurk'),(4414052,'Groene jurk volant','Groene jurk met volant en lint.','100% katoen','Groen','92, 98, 104, 110, 116, 122, 128','12,00','assets/images/4414052.jpg','Jurk'),(4542062,'Grijze skinny jeans kat','Grijze skinny jeans met kat op de knie.','74% katoen + 23% polyester + 3% elastaan','Grijs','92, 98, 104, 110, 116, 122, 128','16,99','assets/images/4542062.jpg','jeans'),(4543022,'Lichtblauwe boyfriend jeans','Lichtblauwe boyfriend jeans met lange pijpen. Met opschrift en broderie.','99% katoen + 1% elastaan','Blauw','92, 98, 104, 110, 116, 122, 128','22,99','assets/images/4543022.jpg','jeans'),(4543032,'Blauwe skinny jeans destroyed','Blauwe skinny jeans met lange pijpen. Afgewassen en destroyed look.','98% katoen + 2% elastaan','Blauw','92, 98, 104, 110, 116, 122, 128','22,99','assets/images/4543032.jpg','jeans'),(4892012,'Donkerblauwe jogdenim','Donkerblauwe broek in comfortable jogdenim met lange pijpen.','83% katoen + 16% polyester + 1% elastaan','Blauw','92, 98, 104, 110, 116, 122, 128','14,00','assets/images/4892012.jpg','jeans'),(4892022,'Blauwe jegging','Blauwe jegging. ','77% katoen + 21% polyester + 2% elastaan','Blauw','92, 98, 104, 110, 116, 122, 128','14,00','assets/images/4892022.jpg','jeans'),(4893012,'Lichtblauwe jogdenim','Lichtblauwe jogdenim met lange pijpen. ','83% katoen + 16% polyester','Blauw','92, 98, 104, 110, 116, 122, 128','16,99','assets/images/4893012.jpg','jeans');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-23 13:36:03
