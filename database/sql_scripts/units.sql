PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS units;
CREATE TABLE units (unit_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, unit VARCHAR (10) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;