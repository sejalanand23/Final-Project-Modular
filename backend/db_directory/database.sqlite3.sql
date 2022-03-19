BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(15),
	"email"	VARCHAR(255),
	"password"	VARCHAR(255),
	"active"	BOOLEAN,
	"fs_uniquifier"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("id"),
	UNIQUE("email"),
	UNIQUE("fs_uniquifier")
);
DROP TABLE IF EXISTS "role";
CREATE TABLE IF NOT EXISTS "role" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(80),
	"description"	VARCHAR(255),
	UNIQUE("name"),
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "card";
CREATE TABLE IF NOT EXISTS "card" (
	"card_id"	INTEGER NOT NULL,
	"card_front"	VARCHAR(100) NOT NULL,
	"card_back"	VARCHAR(100) NOT NULL,
	"difficulty"	VARCHAR(100),
	PRIMARY KEY("card_id")
);
DROP TABLE IF EXISTS "deck";
CREATE TABLE IF NOT EXISTS "deck" (
	"deck_id"	INTEGER NOT NULL,
	"deck_name"	VARCHAR(100) NOT NULL,
	"deck_total_score"	INTEGER,
	"deck_average_score"	FLOAT,
	PRIMARY KEY("deck_id")
);
DROP TABLE IF EXISTS "role_users";
CREATE TABLE IF NOT EXISTS "role_users" (
	"user_id"	INTEGER,
	"role_id"	INTEGER,
	FOREIGN KEY("user_id") REFERENCES "user"("id"),
	FOREIGN KEY("role_id") REFERENCES "role"("id")
);
DROP TABLE IF EXISTS "user_deck_relation";
CREATE TABLE IF NOT EXISTS "user_deck_relation" (
	"correct"	INTEGER,
	"time"	VARCHAR(100),
	"quiz_count"	INTEGER,
	"user_deck_relation_id"	INTEGER NOT NULL,
	"userUCR_foreignid"	INTEGER NOT NULL,
	"deckUCR_foreignid"	INTEGER NOT NULL,
	PRIMARY KEY("user_deck_relation_id"),
	FOREIGN KEY("userUCR_foreignid") REFERENCES "user"("id"),
	FOREIGN KEY("deckUCR_foreignid") REFERENCES "deck"("deck_id")
);
DROP TABLE IF EXISTS "card_deck_relation";
CREATE TABLE IF NOT EXISTS "card_deck_relation" (
	"card_deck_relation_id"	INTEGER NOT NULL,
	"cardCDR_foreignid"	INTEGER NOT NULL,
	"deckCDR_foreignid"	INTEGER NOT NULL,
	PRIMARY KEY("card_deck_relation_id"),
	FOREIGN KEY("cardCDR_foreignid") REFERENCES "card"("card_id"),
	FOREIGN KEY("deckCDR_foreignid") REFERENCES "deck"("deck_id")
);
COMMIT;
