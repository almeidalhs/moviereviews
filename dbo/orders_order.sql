create table orders_order
(
    id           bigint identity
        primary key,
    total_amount numeric(10, 2) not null,
    created_at   datetimeoffset not null,
    status       nvarchar(20)   not null,
    user_id      int            not null
        constraint orders_order_user_id_e9b59eb1_fk_auth_user_id
            references auth_user
)
go

create index orders_order_user_id_e9b59eb1
    on orders_order (user_id)
go

