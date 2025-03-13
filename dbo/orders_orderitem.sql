create table orders_orderitem
(
    id       bigint identity
        primary key,
    quantity int           not null
        constraint orders_orderitem_quantity_b5ee8808_check
            check ([quantity] >= 0),
    price    numeric(6, 2) not null,
    movie_id bigint        not null
        constraint orders_orderitem_movie_id_6b61c196_fk_movie_movie_id
            references movie_movie,
    order_id bigint        not null
        constraint orders_orderitem_order_id_fe61a34d_fk_orders_order_id
            references orders_order
)
go

create index orders_orderitem_movie_id_6b61c196
    on orders_orderitem (movie_id)
go

create index orders_orderitem_order_id_fe61a34d
    on orders_orderitem (order_id)
go

