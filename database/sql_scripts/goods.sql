PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS goods;
CREATE TABLE goods (good_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, good_name VARCHAR (50) NOT NULL,
good_unit INTEGER, good_cat INTEGER,
FOREIGN KEY (good_unit) REFERENCES units (unit_id), FOREIGN KEY(good_cat) REFERENCES categories (category_id));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;