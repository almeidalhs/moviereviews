create table movie_review
(
    id         bigint identity
        primary key,
    text       nvarchar(max) not null,
    date       date          not null,
    watchAgain bit           not null,
    movie_id   bigint        not null
        constraint movie_review_movie_id_43bc85b0_fk_movie_movie_id
            references movie_movie,
    user_id    int           not null
        constraint movie_review_user_id_511299d9_fk_auth_user_id
            references auth_user
)
go

create index movie_review_user_id_511299d9
    on movie_review (user_id)
go

create index movie_review_movie_id_43bc85b0
    on movie_review (movie_id)
go

