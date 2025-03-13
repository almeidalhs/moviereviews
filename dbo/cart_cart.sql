create table cart_cart
(
    id         bigint identity
        primary key,
    created_at datetimeoffset not null,
    user_id    int            not null
        unique
        constraint cart_cart_user_id_9b4220b9_fk_auth_user_id
            references auth_user
)
go

