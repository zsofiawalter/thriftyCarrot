CREATE TABLE Users (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    email VARCHAR (255) NOT NULL,
    password VARCHAR(255) NOT NULL, 
    firstname VARCHAR(30) NOT NULL, 
    lastname VARCHAR(30) NOT NULL, 
    birthdate VARCHAR(25)
);

CREATE TABLE Products (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(12,2) NOT NULL, 
    category VARCHAR(20) NOT NULL,
    store VARCHAR(15) NOT NULL,
    last_update timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
);

CREATE TABLE Preferences (
    uid INT NOT NULL REFERENCES Users(id),
    pid INT NOT NULL REFERENCES Products(id),
    like_dislike BOOLEAN,
    time_created timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
    PRIMARY KEY(uid, pid)
);

-- Stores current carts of users
CREATE TABLE Carts (
    uid INT NOT NULL REFERENCES Users(id),
    pid INT NOT NULL REFERENCES Products(id),
    quantity INT,
    PRIMARY KEY(uid, pid)
);

-- Stores users old carts
CREATE TABLE OldCarts (
    cid INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    uid INT NOT NULL REFERENCES Users(id),
    cart_name VARCHAR(30) NOT NULL,
    time_created timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
);

-- Stores old cart contents
CREATE TABLE OldCartContents (
    cid INT NOT NULL REFERENCES OldCarts(cid),
    pid INT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    price DECIMAL(12,2) NOT NULL, 
    category VARCHAR(15) NOT NULL,
    store VARCHAR (15) NOT NULL,
    PRIMARY KEY(cid, pid)
);


-- -- Initial tables provided by skeleton
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
