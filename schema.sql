drop table if exists posts;
create table posts(
    id integer primary key autoincrement,
    created timestamp not null default current_timestamp,
    title text not null,
    content text not null

);
drop table if exists users;
create table users(
    username text primary key not null,
    email text  not null,
    firstname text not null,
    lastname text not null,
    psw text not null,
    CONSTRAINT name_unique UNIQUE (username, email)
)