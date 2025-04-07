CREATE DATABASE  IF NOT EXISTS `tasks_py` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tasks_py`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: tasks_py
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user_tasks`
--

DROP TABLE IF EXISTS `user_tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_tasks` (
  `Task_id` int NOT NULL AUTO_INCREMENT,
  `User_id` int NOT NULL,
  `Task_name` varchar(30) DEFAULT NULL,
  `Due_date` date NOT NULL,
  `Due_time` time NOT NULL,
  `Priotity` enum('Normal','Medium','High') NOT NULL,
  `Status` enum('Pending','In Progress','Completed') NOT NULL,
  `Comments` text,
  PRIMARY KEY (`Task_id`),
  KEY `User_id` (`User_id`),
  CONSTRAINT `user_tasks_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `users` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_tasks`
--

LOCK TABLES `user_tasks` WRITE;
/*!40000 ALTER TABLE `user_tasks` DISABLE KEYS */;
INSERT INTO `user_tasks` VALUES (1,1,'Pyhton Final Project','2024-05-02','00:00:00','High','In Progress','Send documents'),(2,1,'DBMS Project','2024-04-24','13:00:00','High','Completed','Send script and documentation'),(3,1,'Stats Final Exam','2024-04-29','15:00:00','High','Completed',''),(4,1,'Composition Exam','2024-04-29','11:00:00','High','Completed','Essay'),(5,1,'Dinner','2024-05-03','18:00:00','Normal','Pending','Tulun restaurant'),(6,1,'Pyhton Quiz','2024-04-19','20:00:00','Normal','Completed','chapters 9 to 12'),(7,1,'Composition Essay','2024-04-15','11:00:00','Medium','Completed','create draft'),(8,1,'DBMS Final Exam','2024-04-30','00:00:00','High','Completed','pp from 1 to 9'),(9,1,'Check python project','2024-04-30','15:00:00','Normal','Pending','check for errors before sending');
/*!40000 ALTER TABLE `user_tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `Account_name` varchar(40) DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL,
  `Password` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'XimenaR','ximenaruiz2006@gmail.com','$2b$12$dfgcGAWcDvcsZkWVTM4Rh.pqNACYgkzLLoRtOyaX6tD8cnxIKJVRq');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'tasks_py'
--

--
-- Dumping routines for database 'tasks_py'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 17:30:37
