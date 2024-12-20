-- Desc: Create a database and a table with a primary key and a foreign key
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` ( 
    PRIMARY KEY(`id`),
     `id` INT NOT NULL AUTO_INCREMENT,
     `state_id` INT NOT NULL,
     `name` VARCHAR(256) NOT NULL,
     FOREIGN KEY(`state_id`)
     REFERENCES `hbtn_0d_usa`.`states`(`id`)
     );
