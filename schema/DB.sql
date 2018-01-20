-- user table, username must be unique
create table if not exists `user` (
    `id` int unsigned auto_increment,
    `username` varchar(255) not null,
    `password` varchar(255) not null,
    `created_at` timestamp default current_timestamp,
    `updated_at` timestamp default now() on update now(),
    primary key(`id`),
    unique index `index_username`(`username`)
)ENGINE InnoDB default charset=utf8;