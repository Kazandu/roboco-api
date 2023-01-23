BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "errors" (
	"id"	INTEGER UNIQUE,
	"videolink"	TEXT UNIQUE,
	"errortype"	TEXT,
	"errortime"	TEXT,
	"errortext"	TEXT
);
CREATE TABLE IF NOT EXISTS "errortypes" (
	"ID"	INTEGER UNIQUE,
	"errorname"	TEXT,
	"keystring"	TEXT
);
CREATE TABLE IF NOT EXISTS "batchdata" (
	"id"	INTEGER NOT NULL UNIQUE,
	"videolink"	TEXT NOT NULL UNIQUE,
	"state"	TEXT DEFAULT 'NEW',
	"dateadded"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "archive" (
	"id"	INTEGER NOT NULL UNIQUE,
	"videolink"	INTEGER NOT NULL UNIQUE,
	"state"	INTEGER,
	"datecompleted"	INTEGER,
	PRIMARY KEY("id")
);
COMMIT;
