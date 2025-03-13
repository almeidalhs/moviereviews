create table auth_user_user_permissions
(
    id            bigint identity
        primary key,
    user_id       int not null
        constraint auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id
            references auth_user,
    permission_id int not null
        constraint auth_user_user_permissions_permission_id_1fbb5f2c_fk_auth_permission_id
            references auth_permission
)
go

create unique index auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
    on auth_user_user_permissions (user_id, permission_id)
    where [user_id] IS NOT NULL AND [permission_id] IS NOT NULL
go

create index auth_user_user_permissions_permission_id_1fbb5f2c
    on auth_user_user_permissions (permission_id)
go

create index auth_user_user_permissions_user_id_a95ead1b
    on auth_user_user_permissions (user_id)
go

