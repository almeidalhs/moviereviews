create table auth_user
(
    id           int identity
        primary key,
    password     nvarchar(128)  not null,
    last_login   datetimeoffset,
    is_superuser bit            not null,
    username     nvarchar(150)  not null
        constraint auth_user_username_6821ab7c_uniq
            unique,
    first_name   nvarchar(150)  not null,
    last_name    nvarchar(150)  not null,
    email        nvarchar(254)  not null,
    is_staff     bit            not null,
    is_active    bit            not null,
    date_joined  datetimeoffset not null
)
go

