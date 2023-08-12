-- MySQL-Client Initialization Template File
-- Update the file as per Requirement

CREATE DATABASE IF NOT EXISTS database;

-- similarly multiple database can be created as required
-- CREATE DATABASE IF NOT EXISTS template;

-- write command below to create dummy tables
USE database;

DROP TABLE IF EXISTS `table`;

CREATE TABLE `table` (
  `UUID`       varchar(64)  NOT NULL,
  `FirstName`  varchar(255) NOT NULL,
  `FamilyName` varchar(255) NOT NULL,

  PRIMARY KEY (`UUID`),
  UNIQUE KEY `UUID` (`UUID`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- use mysql:8.0.26 for COLLATE=utf8mb4_0900_ai_ci

LOCK TABLES `table` WRITE;

INSERT INTO `table` VALUES
  ('5ffe4050-d959-46ec-a8a5-c1a0040c9186','Debmalya','Pramanik'),
  ('71c75892-71b0-4381-89ba-b8bf64e38974', 'John', 'Doe');

UNLOCK TABLES;
