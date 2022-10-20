-- Feel free to modify this file to match your development goal.
-- Here we only create 3 tables for demo purpose.

CREATE TABLE User(
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    email VARCHAR (255) NOT NULL
    password VARCHAR(255) NOT NULL, 
    firstname VARCHAR(30) NOT NULL, 
    lastname VARCHAR(30) NOT NULL, 
    birthdate VARCHAR(25),
);

CREATE TABLE Products(
    id INTEGER(10) NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    name VARCHAR(30) NOT NULL,
    price DECIMAL(12,2) NOT NULL, 
    category VARCHAR(15) NOT NULL,
    store VARCHAR(15) NOT NULL,
    last_update VARCHAR (10) NOT NULL
);

CREATE TABLE Preference(
    uid INTEGER(10) NOT NULL REFERENCES User(uid),
    pid INTEGER(10) NOT NULL REFERENCES Products(id),
    like_dislike BOOLEAN
    PRIMARY KEY(uid, pid)
);

-- Stores current carts of users
CREATE TABLE Cart(
    uid INTEGER(10) NOT NULL REFERENCES User(id),
    pid INTEGER(10) NOT NULL REFERENCES Products(id),
    quantity INTEGER(2),
    PRIMARY KEY(uid, pid)
);

-- Stores users old carts
CREATE TABLE OldCarts(
    cid INTEGER(10) NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    uid INTEGER(10) NOT NULL REFERENCES User(uid),
    pid INTEGER(10) NOT NULL,
    cart_name VARCHAR(30) NOT NULL, 
    product_name VARCHAR(30) NOT NULL,
    price DECIMAL(12,2) NOT NULL, 
    category VARCHAR(15) NOT NULL,
    store VARCHAR (15) NOT NULL,
    time_created timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
);


-- Initial tables provided by skeleton
-- CREATE TABLE Users (
--     id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
--     email VARCHAR UNIQUE NOT NULL,
--     password VARCHAR(255) NOT NULL,
--     firstname VARCHAR(255) NOT NULL,
--     lastname VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE Products (
--     id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
--     name VARCHAR(255) UNIQUE NOT NULL,
--     price DECIMAL(12,2) NOT NULL,
--     available BOOLEAN DEFAULT TRUE
-- );

-- CREATE TABLE Purchases (
--     id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
--     uid INT NOT NULL REFERENCES Users(id),
--     pid INT NOT NULL REFERENCES Products(id),
--     time_purchased timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
-- );
