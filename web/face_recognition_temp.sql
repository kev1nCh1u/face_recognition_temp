-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1:3306
-- 產生時間： 
-- 伺服器版本： 5.7.26
-- PHP 版本： 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `face_recognition_temp`
--

-- --------------------------------------------------------

--
-- 資料表結構 `face_recognition_temp`
--

DROP TABLE IF EXISTS `face_recognition_temp`;
CREATE TABLE IF NOT EXISTS `face_recognition_temp` (
  `name` char(50) DEFAULT NULL,
  `temp` char(50) DEFAULT NULL,
  `time` char(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `face_recognition_temp`
--

INSERT INTO `face_recognition_temp` (`name`, `temp`, `time`) VALUES
('kevin', '36', '2020-07-25 14:31:42'),
('amy', '36.6', '2020-07-25 21:01:54.634130');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
