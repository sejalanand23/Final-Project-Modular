from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields
from sqlalchemy.orm import backref
from sympy import sec
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security.models import fsqla_v2 as fsqla
from flask_security import UserMixin, RoleMixin
import jwt
import datetime

db = SQLAlchemy()

role_users = db.Table('role_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

# class User(db.Model,fsqla.FsUserMixin):
class User(db.Model,UserMixin):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(15)) 
  email = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255))
  active = db.Column(db.Boolean())
  fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) 
  roles = db.relationship('Role', secondary=role_users,backref=db.backref('users', lazy='dynamic'))
  deck_user = db.relationship('UserDeckRelation', backref = 'user',cascade="all,delete")

  def encode_auth_token(self, user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            'some-secret-key',
            algorithm='HS256'
        )
    except Exception as e:
        return e

  @staticmethod
  def decode_auth_token(auth_token):
      """
      Decodes the auth token
      :param auth_token:
      :return: integer|string
      """
      try:
          payload = jwt.decode(auth_token,'some-secret-key' )
          return payload['sub']
      except jwt.ExpiredSignatureError:
          return 'Signature expired. Please log in again.'
      except jwt.InvalidTokenError:
          return 'Invalid token. Please log in again.'

user_fields = {
    'id' : fields.Integer,
    'email' : fields.String,
    'password' : fields.String
}

# class Role(db.Model, fsqla.FsRoleMixin):
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
  difficulty = db.Column(db.String(100))
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
  deck_total_score = db.Column(db.Integer)
  deck_average_score = db.Column(db.Float)
  correct = db.Column(db.Integer)
  time = db.Column(db.String(100))
  quiz_count = db.Column(db.Integer)
  card_deck = db.relationship('CardDeckRelation', backref = 'deck',cascade="all,delete")
  user_deck = db.relationship('UserDeckRelation', backref = 'deck',cascade="all,delete")

deck_fields = {
    'deck_id' : fields.Integer,
    'deck_name' : fields.String,
    'deck_total_score' : fields.Integer,
    'deck_average_score' : fields.Float,
    'correct' : fields.Integer,
    'time' : fields.String,
    'quiz_count' : fields.Integer,
}
  
class UserDeckRelation(db.Model):
  __tablename__ = 'user_deck_relation'
  correct = db.Column(db.Integer)
  time = db.Column(db.String(100))
  quiz_count = db.Column(db.Integer)
  user_deck_relation_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  userUCR_foreignid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
  deckUCR_foreignid = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable = False)

user_deck_fields = {
  'correct' : fields.Integer,
  'time' : fields.String,
  'quiz_count' : fields.Integer,
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