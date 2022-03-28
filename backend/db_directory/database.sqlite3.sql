BEGIN TRANSACTION;
DROP TABLE IF EXISTS "role";
CREATE TABLE IF NOT EXISTS "role" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(80),
	"description"	VARCHAR(255),
	UNIQUE("name"),
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "role_users";
CREATE TABLE IF NOT EXISTS "role_users" (
	"user_id"	INTEGER,
	"role_id"	INTEGER,
	FOREIGN KEY("role_id") REFERENCES "role"("id"),
	FOREIGN KEY("user_id") REFERENCES "user"("id")
);
DROP TABLE IF EXISTS "card_deck_relation";
CREATE TABLE IF NOT EXISTS "card_deck_relation" (
	"card_deck_relation_id"	INTEGER NOT NULL,
	"cardCDR_foreignid"	INTEGER NOT NULL,
	"deckCDR_foreignid"	INTEGER NOT NULL,
	FOREIGN KEY("deckCDR_foreignid") REFERENCES "deck"("deck_id"),
	FOREIGN KEY("cardCDR_foreignid") REFERENCES "card"("card_id"),
	PRIMARY KEY("card_deck_relation_id")
);
DROP TABLE IF EXISTS "user_deck_relation";
CREATE TABLE IF NOT EXISTS "user_deck_relation" (
	"user_deck_relation_id"	INTEGER NOT NULL,
	"userUCR_foreignid"	INTEGER NOT NULL,
	"deckUCR_foreignid"	INTEGER NOT NULL,
	FOREIGN KEY("userUCR_foreignid") REFERENCES "user"("id"),
	FOREIGN KEY("deckUCR_foreignid") REFERENCES "deck"("deck_id"),
	PRIMARY KEY("user_deck_relation_id")
);
DROP TABLE IF EXISTS "deck";
CREATE TABLE IF NOT EXISTS "deck" (
	"deck_id"	INTEGER NOT NULL,
	"deck_name"	VARCHAR(100) NOT NULL,
	"deck_total_score"	FLOAT DEFAULT 0,
	"deck_average_score"	FLOAT,
	"correct"	INTEGER,
	"time"	TEXT,
	"quiz_count"	INTEGER DEFAULT 0,
	PRIMARY KEY("deck_id")
);
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"email"	VARCHAR(255),
	"password"	VARCHAR(255),
	"active"	BOOLEAN,
	"fs_uniquifier"	VARCHAR(255),
	UNIQUE("email"),
	PRIMARY KEY("id"),
	UNIQUE("fs_uniquifier")
);
DROP TABLE IF EXISTS "card";
CREATE TABLE IF NOT EXISTS "card" (
	"card_id"	INTEGER NOT NULL,
	"card_front"	VARCHAR(100) NOT NULL,
	"card_back"	VARCHAR(100) NOT NULL,
	PRIMARY KEY("card_id")
);
INSERT INTO "card_deck_relation" VALUES (4,4,2);
INSERT INTO "card_deck_relation" VALUES (5,5,2);
INSERT INTO "card_deck_relation" VALUES (6,6,2);
INSERT INTO "card_deck_relation" VALUES (7,7,2);
INSERT INTO "card_deck_relation" VALUES (8,8,3);
INSERT INTO "card_deck_relation" VALUES (9,9,3);
INSERT INTO "card_deck_relation" VALUES (10,10,3);
INSERT INTO "card_deck_relation" VALUES (11,11,3);
INSERT INTO "card_deck_relation" VALUES (12,12,4);
INSERT INTO "card_deck_relation" VALUES (13,13,4);
INSERT INTO "card_deck_relation" VALUES (14,14,4);
INSERT INTO "card_deck_relation" VALUES (15,15,3);
INSERT INTO "card_deck_relation" VALUES (19,19,3);
INSERT INTO "card_deck_relation" VALUES (21,21,6);
INSERT INTO "card_deck_relation" VALUES (22,22,6);
INSERT INTO "card_deck_relation" VALUES (23,23,5);
INSERT INTO "card_deck_relation" VALUES (24,24,5);
INSERT INTO "card_deck_relation" VALUES (25,25,5);
INSERT INTO "card_deck_relation" VALUES (26,26,5);
INSERT INTO "user_deck_relation" VALUES (2,1,2);
INSERT INTO "user_deck_relation" VALUES (3,1,3);
INSERT INTO "user_deck_relation" VALUES (4,3,4);
INSERT INTO "user_deck_relation" VALUES (5,1,5);
INSERT INTO "user_deck_relation" VALUES (6,5,6);
INSERT INTO "deck" VALUES (2,'Opposite Words',125.0,62.5,25,'Sat Mar 26 01:23:27 2022',2);
INSERT INTO "deck" VALUES (3,'Indian Spices',110.0,53.3333333333333,50,'Sat Mar 26 01:18:17 2022',2);
INSERT INTO "deck" VALUES (4,'Spices',100.0,50.0,0,'Sat Mar 26 01:24:38 2022',2);
INSERT INTO "deck" VALUES (5,'Chemistry',175.0,58.3333333333333,75,'Sun Mar 27 22:53:03 2022',3);
INSERT INTO "deck" VALUES (6,'games',83.0,41.5,50,'Sat Mar 26 18:39:30 2022',2);
INSERT INTO "deck" VALUES (8,'Another test',0.0,NULL,NULL,NULL,0);
INSERT INTO "user" VALUES (1,'test@abc.com','$2b$12$VCNlJx0N2vHqB/jy6caV3.lvpS4PU9c6qO3NIYZ0i36Xs9bmoEvmm',1,'hadbsdjhdbdjbj');
INSERT INTO "user" VALUES (3,'new@abc.com','$2b$12$o.VEgakjKNQp0Dm8Y.cNeu7GjX3yE.3uvNTSOR4a8MaxviYWNH7l2',1,'11cdb632bc124099936553a3f4fb42fa');
INSERT INTO "user" VALUES (4,'sejalanand23@gmail.com','$2b$12$5kTq04tyf6fuFAMPRit4Ze0N68Kk9JGK8qS0nGEFQ8lkK61D4eDA2',1,'c0d93f51295f410899f229dbf52da9da');
INSERT INTO "user" VALUES (5,'dryyfdft098@gmail.com','$2b$12$neoOKr7qdzRNy86VjWhCTuXAZXbgjHhmB40UO9mPZJRC1yH0JpYkW',1,'b14cf3441880415baf8acedee4fa0873');
INSERT INTO "user" VALUES (6,'test1@abc.com','$2b$12$qk2v19aT0T9yhricZPWUr.Jj3.O70GPt5b3oOy9X4JbSdv.TdgiwO',1,'190202859a904a82834da3132dd57750');
INSERT INTO "card" VALUES (4,'Tall','Short');
INSERT INTO "card" VALUES (5,'Fat','Thin');
INSERT INTO "card" VALUES (6,'Dark','Light');
INSERT INTO "card" VALUES (7,'Far','Near');
INSERT INTO "card" VALUES (8,'dalchini','cinnamon');
INSERT INTO "card" VALUES (9,'ajwain','carrom seeds');
INSERT INTO "card" VALUES (10,'haldi','turmeric');
INSERT INTO "card" VALUES (11,'namak','salt');
INSERT INTO "card" VALUES (12,'Dalchini','Cinnamon');
INSERT INTO "card" VALUES (13,'Dhaniya','Coriander');
INSERT INTO "card" VALUES (14,'Lal Mirch Powder','Red Chilli Powder');
INSERT INTO "card" VALUES (15,'jeera','cumin');
INSERT INTO "card" VALUES (19,'laung','clove');
INSERT INTO "card" VALUES (21,'dota 2','pc game');
INSERT INTO "card" VALUES (22,'csgo','most famous');
INSERT INTO "card" VALUES (23,'H2O','Water');
INSERT INTO "card" VALUES (24,'O','Oxygen');
INSERT INTO "card" VALUES (25,'Fe','Iron');
INSERT INTO "card" VALUES (26,'Na','Sodium');
COMMIT;
