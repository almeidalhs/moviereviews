create table movie_movie
(
    id          bigint identity
        primary key,
    title       nvarchar(100) not null,
    description nvarchar(250) not null,
    image       nvarchar(100) not null,
    url         nvarchar(200) not null,
    price       numeric(6, 2) not null
)
go

