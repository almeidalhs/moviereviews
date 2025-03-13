create table django_session
(
    session_key  nvarchar(40)   not null
        primary key,
    session_data nvarchar(max)  not null,
    expire_date  datetimeoffset not null
)
go

create index django_session_expire_date_a5c62663
    on django_session (expire_date)
go

