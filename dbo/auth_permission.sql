create table auth_permission
(
    id              int identity
        primary key,
    name            nvarchar(255) not null,
    content_type_id int           not null
        constraint auth_permission_content_type_id_2f476e4b_fk_django_content_type_id
            references django_content_type,
    codename        nvarchar(100) not null
)
go

create unique index auth_permission_content_type_id_codename_01ab375a_uniq
    on auth_permission (content_type_id, codename)
    where [content_type_id] IS NOT NULL AND [codename] IS NOT NULL
go

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id)
go

