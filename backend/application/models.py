from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields
from flask_security import UserMixin, RoleMixin
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

role_users = db.Table('role_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
class User(db.Model,UserMixin):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255))
  active = db.Column(db.Boolean())
  fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) 
  roles = db.relationship('Role', secondary=role_users,backref=db.backref('users', lazy='dynamic'))
  deck_user = db.relationship('UserDeckRelation', backref = 'user',cascade="all,delete")

user_fields = {
    'id' : fields.Integer,
    'email' : fields.String,
    'password' : fields.String
}

class Role(db.Model,RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Card(db.Model):
  __tablename__ = 'card'
  card_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  card_front = db.Column(db.String(100), nullable = False)
  card_back = db.Column(db.String(100), nullable = False)
  deck_card = db.relationship('CardDeckRelation', backref = 'card',cascade="all,delete")

card_fields = {
    'card_id' : fields.Integer,
    'card_front' : fields.String,
    'card_back' : fields.String,
    'difficulty' : fields.String
}


class Deck(db.Model):
  __tablename__ = 'deck'
  deck_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  deck_name = db.Column(db.String(100), nullable = False)
  deck_total_score = db.Column(db.Float,default = 0)
  deck_average_score = db.Column(db.Float)
  correct = db.Column(db.Integer)
  time = db.Column(db.String(100))
  quiz_count = db.Column(db.Integer,default = 0)
  card_deck = db.relationship('CardDeckRelation', backref = 'deck',cascade="all,delete")
  user_deck = db.relationship('UserDeckRelation', backref = 'deck',cascade="all,delete")



deck_fields = {
    'deck_id' : fields.Integer,
    'deck_name' : fields.String,
    'deck_total_score' : fields.Float,
    'deck_average_score' : fields.Float,
    'correct' : fields.Integer,
    'time' : fields.String,
    'quiz_count' : fields.Integer,
}
  
class UserDeckRelation(db.Model):
  __tablename__ = 'user_deck_relation'
  user_deck_relation_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  userUCR_foreignid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
  deckUCR_foreignid = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable = False)

user_deck_fields = {
  'user_deck_relation_id' : fields.Integer,
  'userUCR_foreignid' : fields.Integer,
  'deckUCR_foreignid' : fields.Integer
}

class CardDeckRelation(db.Model):
  __tablename__ = 'card_deck_relation'
  card_deck_relation_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  cardCDR_foreignid = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable = False)
  deckCDR_foreignid = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable = False)

card_deck_fields = {
  'card_deck_relation_id' : fields.Integer,
  'cardCDR_foreignid' : fields.Integer,
  'deckCDR_foreignid' : fields.Integer
}

class DeckSchema(ma.SQLAlchemySchema):
  class Meta:
    model = Deck
  
  deck_id = ma.auto_field()
  deck_name = ma.auto_field()
  deck_total_score = ma.auto_field()
  deck_average_score = ma.auto_field()
  correct = ma.auto_field()
  time = ma.auto_field()
  quiz_count = ma.auto_field()

class CardSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Card