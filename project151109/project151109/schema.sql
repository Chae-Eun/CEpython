drop table if exists user;
create table user(
user_no integer primary key autoincrement,
userid string not null,
username string not null,
userpw string not null
);