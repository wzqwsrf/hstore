create database hstore;
create extension hstore;
create table users(
id serial,
info hstore
);
