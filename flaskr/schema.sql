drop table if exists entries;
create table entries (
  id INT  primary key AUTO_INCREMENT,
  title VARCHAR(20) not null,
  text VARCHAR(40) not null
);