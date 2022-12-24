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
  `msg` varchar(100) DEFAULT NULL,
  `fecha` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `atencion_reclamo`
--

INSERT INTO `atencion_reclamo` (`id_atencion`, `nombres`, `apellido_paterno`, `apellido_materno`, `correo`, `dni`, `telefono`, `msg`, `fecha`) VALUES
(1, 'salas', 'sasla', 'test@test.com', '73813709', '999989999', 'qwwedws c ', NULL, NULL),
(2, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg', NULL),
(3, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg', NULL),
(4, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg', NULL),
(5, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg', NULL),
(6, 'jorge', 'salas', 'sasla', 'dimineko2@gmail.com', '41343968', '1111111', '123asasxascxsa csdfe rg', NULL),
(7, 'test', 'test', 'test', 'test@test.com', '12', '123', 'tweast123', NULL),
(8, 'test', 'test', 'test', 'test@test.com', '12', '123', 'tweast123', NULL),
(9, 'test', 'salas', 'test', 'test@test.com', '73813709', '1111111', 'wqwwqwqw', NULL),
(10, 'jorge', 'salas', 'test', 'test@test.com', '73813709', '999989999', 'ewrewrew', NULL),
(11, 'wweew', 'ewe', 'asas', 'asas@test.com', '123', '123', 'sacxsadcsd', NULL),
(12, '3', '3', '3', '3@test.com', '3', '3', '3', '2022-12-23');

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
(1, '1', '1', '1', '1', '1'),
(99830912, 'Kevin', 'Fernandez', 'Soto', 'kevin@gmail.com', '992307341');

-- --------------------------------------------------------

--
-- Table structure for table `servicio_reclamo`
--

CREATE TABLE `servicio_reclamo` (
  `dni` int(11) DEFAULT NULL,
  `motivo` varchar(100) DEFAULT NULL,
  `detalle` varchar(100) DEFAULT NULL,
  `solicitud` varchar(100) DEFAULT NULL,
  `fecha` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `servicio_reclamo`
--

INSERT INTO `servicio_reclamo` (`dni`, `motivo`, `detalle`, `solicitud`, `fecha`) VALUES
(1, 'asasas', 'asasa', 'asasa', NULL),
(1, '11', '11', '11', NULL),
(1, 'test', 'test', 'test con fecha', '2022-12-23'),
(99830912, 'motivo_reclamo', 'detalle reclamo', 'solicitud reclamo', '2022-12-23');

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
-- Indexes for table `servicio_reclamo`
--
ALTER TABLE `servicio_reclamo`
  ADD KEY `reclamo_cliente` (`dni`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `atencion_reclamo`
--
ALTER TABLE `atencion_reclamo`
  MODIFY `id_atencion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `servicio_reclamo`
--
ALTER TABLE `servicio_reclamo`
  ADD CONSTRAINT `reclamo_cliente` FOREIGN KEY (`dni`) REFERENCES `cliente` (`dni`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
