CREATE SCHEMA teach;

CREATE TABLE teach.ducks
(
    id serial primary key,
    name text not null,
    age smallint not null,
    address text not null,
    favorite_pond text,
    duck_created timestamptz not null,
    duck_updated timestamptz
);

CREATE INDEX duck_nameidx on teach.ducks(name);


