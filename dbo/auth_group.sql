create table auth_group
(
    id   int identity
        primary key,
    name nvarchar(150) not null
        constraint auth_group_name_a6ea08ec_uniq
            unique
)
go

