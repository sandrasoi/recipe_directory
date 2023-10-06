-- file: recipes_table.sql



CREATE TABLE recipes (
id SERIAL PRIMARY KEY,
name text,
cooking_time text,
rating int
);