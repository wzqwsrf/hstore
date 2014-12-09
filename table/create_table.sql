create database hstore;
create extension hstore;
create table(
id serial,
info hstore
);