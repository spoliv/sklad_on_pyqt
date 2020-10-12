PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS vendors;
CREATE TABLE vendors (vendor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, vendor_name VARCHAR (50) NOT NULL,
vendor_ownerchipform VARCHAR (50) NOT NULL, vendor_address VARCHAR (200) NOT NULL, vendor_phone VARCHAR (20) NOT NULL,
vendor_email VARCHAR (20) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;