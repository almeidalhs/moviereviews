create table django_migrations
(
    id      bigint identity
        primary key,
    app     nvarchar(255)  not null,
    name    nvarchar(255)  not null,
    applied datetimeoffset not null
)
go

