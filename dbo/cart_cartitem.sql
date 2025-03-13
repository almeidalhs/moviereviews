create table cart_cartitem
(
    id       bigint identity
        primary key,
    quantity int    not null
        constraint cart_cartitem_quantity_680030c0_check
            check ([quantity] >= 0),
    cart_id  bigint not null
        constraint cart_cartitem_cart_id_370ad265_fk_cart_cart_id
            references cart_cart,
    movie_id bigint not null
        constraint cart_cartitem_movie_id_516c3a8e_fk_movie_movie_id
            references movie_movie
)
go

create index cart_cartitem_movie_id_516c3a8e
    on cart_cartitem (movie_id)
go

create index cart_cartitem_cart_id_370ad265
    on cart_cartitem (cart_id)
go

