create table django_content_type
(
    id        int identity
        primary key,
    app_label nvarchar(100) not null,
    model     nvarchar(100) not null
)
go

create unique index django_content_type_app_label_model_76bd3d3b_uniq
    on django_content_type (app_label, model)
    where [app_label] IS NOT NULL AND [model] IS NOT NULL
go

