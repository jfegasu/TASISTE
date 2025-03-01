DROP DATABASE IF EXISTS HR;
CREATE DATABASE HR;
USE HR
CREATE TABLE IF NOT EXISTS `regions` (
  `region_id` int(11) unsigned NOT NULL,
  `region_name` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `countries` (
  `country_id` char(2) NOT NULL,
  `country_name` varchar(40) DEFAULT NULL,
  `region_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`country_id`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `countries_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `regions` (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `jobs` (
  `job_id` varchar(10) NOT NULL,
  `job_title` varchar(35) NOT NULL,
  `min_salary` decimal(8,0) unsigned DEFAULT NULL,
  `max_salary` decimal(8,0) unsigned DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `employees` (
  `employee_id` int(11) unsigned NOT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `hire_date` date NOT NULL,
  `job_id` varchar(10) NOT NULL,
  `salary` decimal(8,2) NOT NULL,
  `commission_pct` decimal(2,2) DEFAULT NULL,
  `manager_id` int(11) unsigned DEFAULT NULL,
  `department_id` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `job_id` (`job_id`),
  KEY `department_id` (`department_id`),
  KEY `manager_id` (`manager_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`),
  CONSTRAINT `employees_ibfk_3` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `job_history` (
  `employee_id` int(11) unsigned NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `job_id` varchar(10) NOT NULL,
  `department_id` int(11) unsigned NOT NULL,
  UNIQUE KEY `employee_id` (`employee_id`,`start_date`),
  KEY `job_id` (`job_id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `job_history_ibfk_2` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `locations` (
  `location_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `street_address` varchar(40) DEFAULT NULL,
  `postal_code` varchar(12) DEFAULT NULL,
  `city` varchar(30) NOT NULL,
  `state_province` varchar(25) DEFAULT NULL,
  `country_id` char(2) NOT NULL,
  PRIMARY KEY (`location_id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3201 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `departments` (
  `department_id` int(11) unsigned NOT NULL,
  `department_name` varchar(30) NOT NULL,
  `manager_id` int(11) unsigned DEFAULT NULL,
  `location_id` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`department_id`),
  KEY `location_id` (`location_id`),
  KEY `manager_id` (`manager_id`),
  CONSTRAINT `departments_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`location_id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `emp_details_view` (
	`employee_id` INT(11) UNSIGNED NOT NULL,
	`job_id` VARCHAR(10) NOT NULL COLLATE 'utf8_general_ci',
	`manager_id` INT(11) UNSIGNED NULL,
	`department_id` INT(11) UNSIGNED NULL,
	`location_id` INT(11) UNSIGNED NULL,
	`country_id` CHAR(2) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(25) NOT NULL COLLATE 'utf8_general_ci',
	`salary` DECIMAL(8,2) NOT NULL,
	`commission_pct` DECIMAL(2,2) NULL,
	`department_name` VARCHAR(30) NOT NULL COLLATE 'utf8_general_ci',
	`job_title` VARCHAR(35) NOT NULL COLLATE 'utf8_general_ci',
	`city` VARCHAR(30) NOT NULL COLLATE 'utf8_general_ci',
	`state_province` VARCHAR(25) NULL COLLATE 'utf8_general_ci',
	`country_name` VARCHAR(40) NULL COLLATE 'utf8_general_ci',
	`region_name` VARCHAR(25) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;
CREATE TABLE IF NOT EXISTS `regions` (
  `region_id` int(11) unsigned NOT NULL,
  `region_name` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


