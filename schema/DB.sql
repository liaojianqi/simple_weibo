-- user table, username must be unique
create table if not exists `user_user` (
    `id` int unsigned auto_increment,
    `username` varchar(255) not null,
    `password` varchar(255) not null,
    `created_at` timestamp default current_timestamp,
    `updated_at` timestamp default now() on update now(),
    primary key(`id`),
    unique index `index_username`(`username`)
)ENGINE InnoDB default charset=utf8;

-- follower table, only store follow relationship, not include be followed relation
create table if not exists `user_follow` (
    `id` int unsigned auto_increment,
    `from_name` varchar(255) not null,
    `to_name` varchar(255) not null,
    `created_at` timestamp default current_timestamp,
    `updated_at` timestamp default now() on update now(),
    primary key(`id`),
    index `index_to`(`to_name`),
    unique index `union_index`(`from_name`, `to_name`)
)ENGINE InnoDB default charset=utf8;