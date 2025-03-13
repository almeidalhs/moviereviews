create table news_news
(
    id       bigint identity
        primary key,
    headline nvarchar(200) not null,
    body     nvarchar(max) not null,
    url      nvarchar(200) not null,
    date     date          not null
)
go

