BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"user_id"	INTEGER NOT NULL,
	"username"	VARCHAR(15) NOT NULL,
	"password"	VARCHAR(15) NOT NULL,
	PRIMARY KEY("user_id"),
	UNIQUE("username")
);
DROP TABLE IF EXISTS "card";
CREATE TABLE IF NOT EXISTS "card" (
	"card_id"	INTEGER NOT NULL,
	"card_front"	VARCHAR(100) NOT NULL,
	"card_back"	VARCHAR(100) NOT NULL,
	"difficulty"	VARCHAR(100),
	UNIQUE("card_front"),
	PRIMARY KEY("card_id")
);
DROP TABLE IF EXISTS "deck";
CREATE TABLE IF NOT EXISTS "deck" (
	"deck_id"	INTEGER NOT NULL,
	"deck_name"	VARCHAR(100) NOT NULL,
	"deck_total_score"	INTEGER,
	"deck_average_score"	FLOAT,
	UNIQUE("deck_name"),
	PRIMARY KEY("deck_id")
);
DROP TABLE IF EXISTS "user_deck_relation";
CREATE TABLE IF NOT EXISTS "user_deck_relation" (
	"correct"	INTEGER,
	"time"	VARCHAR(100),
	"quiz_count"	INTEGER,
	"user_deck_relation_id"	INTEGER NOT NULL,
	"userUCR_foreignid"	INTEGER NOT NULL,
	"deckUCR_foreignid"	INTEGER NOT NULL,
	FOREIGN KEY("deckUCR_foreignid") REFERENCES "deck"("deck_id"),
	FOREIGN KEY("userUCR_foreignid") REFERENCES "user"("user_id"),
	PRIMARY KEY("user_deck_relation_id")
);
DROP TABLE IF EXISTS "card_deck_relation";
CREATE TABLE IF NOT EXISTS "card_deck_relation" (
	"card_deck_relation_id"	INTEGER NOT NULL,
	"cardCDR_foreignid"	INTEGER NOT NULL,
	"deckCDR_foreignid"	INTEGER NOT NULL,
	FOREIGN KEY("cardCDR_foreignid") REFERENCES "card"("card_id"),
	FOREIGN KEY("deckCDR_foreignid") REFERENCES "deck"("deck_id"),
	PRIMARY KEY("card_deck_relation_id")
);
COMMIT;
