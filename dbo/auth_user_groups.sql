create table auth_user_groups
(
    id       bigint identity
        primary key,
    user_id  int not null
        constraint auth_user_groups_user_id_6a12ed8b_fk_auth_user_id
            references auth_user,
    group_id int not null
        constraint auth_user_groups_group_id_97559544_fk_auth_group_id
            references auth_group
)
go

create index auth_user_groups_user_id_6a12ed8b
    on auth_user_groups (user_id)
go

create index auth_user_groups_group_id_97559544
    on auth_user_groups (group_id)
go

create unique index auth_user_groups_user_id_group_id_94350c0c_uniq
    on auth_user_groups (user_id, group_id)
    where [user_id] IS NOT NULL AND [group_id] IS NOT NULL
go

