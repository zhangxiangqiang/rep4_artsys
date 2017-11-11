create database artdb;

use artdb;

-- create table if not exists admin(
--     id int unsigned not null auto_increment key,
--     name varchar(255),
--     pwd char(32),
--     addtime timestamp
-- )engine=InnoDB default charset=utf8;

create table if not exists tag(
    id int unsigned not null auto_increment key,
    name varchar(255),
    info varchar(300),
    addtime timestamp
)engine=InnoDB default charset=utf8;

create table if not exists art(
    id int unsigned not null auto_increment key,
    title varchar(255),
    info varchar(300),
    content mediumtext,
    tag int unsigned,
    img varchar(255),
    addtime timestamp
)engine=InnoDB default charset=utf8;

create table if not exists users(
    id int unsigned not null auto_increment key,
    username varchar(255),
    email varchar(300) not null,
    password varchar(255) not null,
    addtime timestamp
)engine=InnoDB default charset=utf8;
