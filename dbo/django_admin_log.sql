create table django_admin_log
(
    id              int identity
        primary key,
    action_time     datetimeoffset not null,
    object_id       nvarchar(max),
    object_repr     nvarchar(200)  not null,
    action_flag     smallint       not null
        constraint django_admin_log_action_flag_a8637d59_check
            check ([action_flag] >= 0),
    change_message  nvarchar(max)  not null,
    content_type_id int
        constraint django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id
            references django_content_type,
    user_id         int            not null
        constraint django_admin_log_user_id_c564eba6_fk_auth_user_id
            references auth_user
)
go

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id)
go

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id)
go

