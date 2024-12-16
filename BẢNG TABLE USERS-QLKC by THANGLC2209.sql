CREATE DATABASE QLKC;
USE QLKC;


CREATE TABLE USERS (
	 id INT AUTO_INCREMENT PRIMARY KEY,
    EMAIL VARCHAR(100),
    passwords varchar(255),
    Fullname varchar(100),
    role ENUM('admin','user'),
    created_at TIMESTAMP
);
    