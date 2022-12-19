-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 18, 2022 at 11:53 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crm_reclamos`
--

-- --------------------------------------------------------

--
-- Table structure for table `atencion_reclamo`
--

CREATE TABLE `atencion_reclamo` (
  `id_atencion` int(11) NOT NULL,
  `nombres` varchar(45) DEFAULT NULL,
  `apellido_paterno` varchar(45) DEFAULT NULL,
  `apellido_materno` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `dni` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `atencion_reclamo`
--

INSERT INTO `atencion_reclamo` (`id_atencion`, `nombres`, `apellido_paterno`, `apellido_materno`, `correo`, `dni`, `telefono`, `msg`) VALUES
(1, 'salas', 'sasla', 'test@test.com', '73813709', '999989999', 'qwwedws c ', NULL),
(2, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg'),
(3, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg'),
(4, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg'),
(5, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg'),
(6, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg'),
(7, 'test', 'test', 'test', 'test@test.com', '12', '123', 'tweast123'),
(8, 'test', 'test', 'test', 'test@test.com', '12', '123', 'tweast123'),
(9, 'test', 'salas', 'test', 'test@test.com', '73813709', '1111111', 'wqwwqwqw'),
(10, 'jorge', 'salas', 'test', 'test@test.com', '73813709', '999989999', 'ewrewrew'),
(11, 'wweew', 'ewe', 'asas', 'asas@test.com', '123', '123', 'sacxsadcsd');

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `dni` int(11) NOT NULL,
  `nombres` varchar(45) DEFAULT NULL,
  `apellido_paterno` varchar(45) DEFAULT NULL,
  `apellido_materno` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`dni`, `nombres`, `apellido_paterno`, `apellido_materno`, `correo`, `telefono`) VALUES
(1, '1', '1', '1', '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `cliente_reclamo`
--

CREATE TABLE `cliente_reclamo` (
  `dni` int(11) DEFAULT NULL,
  `motivo` varchar(100) DEFAULT NULL,
  `detalle` varchar(100) DEFAULT NULL,
  `solicitud` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cliente_reclamo`
--

INSERT INTO `cliente_reclamo` (`dni`, `motivo`, `detalle`, `solicitud`) VALUES
(1, 'asasas', 'asasa', 'asasa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `atencion_reclamo`
--
ALTER TABLE `atencion_reclamo`
  ADD PRIMARY KEY (`id_atencion`);

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`dni`);

--
-- Indexes for table `cliente_reclamo`
--
ALTER TABLE `cliente_reclamo`
  ADD KEY `reclamo_cliente` (`dni`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `atencion_reclamo`
--
ALTER TABLE `atencion_reclamo`
  MODIFY `id_atencion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cliente_reclamo`
--
ALTER TABLE `cliente_reclamo`
  ADD CONSTRAINT `reclamo_cliente` FOREIGN KEY (`dni`) REFERENCES `cliente` (`dni`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
