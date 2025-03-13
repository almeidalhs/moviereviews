create table auth_group_permissions
(
    id            bigint identity
        primary key,
    group_id      int not null
        constraint auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
            references auth_group,
    permission_id int not null
        constraint auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id
            references auth_permission
)
go

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id)
go

create unique index auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    on auth_group_permissions (group_id, permission_id)
    where [group_id] IS NOT NULL AND [permission_id] IS NOT NULL
go

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id)
go

