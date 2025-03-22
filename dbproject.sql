CREATE DATABASE project;
USE project;
CREATE TABLE Admin(
	Username VARCHAR(20),
    APwd VARCHAR(20)
);
INSERT INTO Admin
(Username,Apwd)
VALUES
("ADMIN","admin"),
("LIT","lit123");

CREATE TABLE  Student(
	Regno INT PRIMARY KEY,
    Name VARCHAR(30),
    Dept VARCHAR(20),
    AccYear VARCHAR(20)
);
INSERT INTO Student
(Regno,Name,Dept,AccYear)
VALUES
(100,"Alok","CSE","2020-2024");
