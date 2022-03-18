from urllib import request
from flask_restful import Resource, Api, marshal
from flask_restful import fields, marshal_with
from flask_restful import reqparse
from flask_security import auth_required
from sympy import re
from application.validation import BusinessValidationError, NotFoundError
from application.models import *
from application.database import db
from flask import current_app as app
import werkzeug
from flask import abort

user_parser = reqparse.RequestParser()
# user_parser.add_argument('user_id',type=int)
user_parser.add_argument('username',type = str,required = True)
user_parser.add_argument('password',type = str)

deck_post_parser = reqparse.RequestParser()
deck_post_parser.add_argument('username',type = str,required = True)
deck_post_parser.add_argument('deck_name',type = str, required = True)

card_parser = reqparse.RequestParser()
card_parser.add_argument('card_id',db.Integer)
card_parser.add_argument('card_front',type = str)
card_parser.add_argument('card_back',type = str)
card_parser.add_argument('difficulty',type = str)

deck_parser = reqparse.RequestParser()
# deck_parser.add_argument('deck_id',db.Integer)
deck_parser.add_argument('deck_name',type = str, required = True)
# deck_parser.add_argument('deck_total_score',type = int)
# deck_parser.add_argument('deck_average_score',type = float)

user_deck_parser = reqparse.RequestParser()
user_deck_parser.add_argument('correct',type=int)
user_deck_parser.add_argument('time',type=str)
user_deck_parser.add_argument('quiz_count',type=int)
user_deck_parser.add_argument('user_deck_relation_id',type = int)
user_deck_parser.add_argument('userUCR_foreignid',type = int)
user_deck_parser.add_argument('deckUCR_foreignid',type = int)

card_deck_parser = reqparse.RequestParser()
card_deck_parser.add_argument('card_deck_relation_id',type = int)
card_deck_parser.add_argument('cardCDR_foreignid',type = int)
card_deck_parser.add_argument('deckCDR_foreignid',type = int)

class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self,username=None):
        if username:
            user = User.query.filter_by(username = username).first()
            if user is None:
                abort(404, "User does not exist")
            else:
                return user, 201
        else:
            user = User.query.all()
            return user, 201
    
    @marshal_with(user_fields)
    def post(self):
        user_args = user_parser.parse_args()
        user = User.query.filter_by(username = user_args['username']).first()
        if user:
            abort(409,"User already exists")
        else:
            u = User(username = user_args['username'],password = user_args['password'])
            db.session.add(u)
            db.session.commit()
            return u, 201


class DeckResource(Resource):
    @marshal_with(deck_fields)
    def get(self,deck_name = None):
        if deck_name:
            deck = Deck.query.filter_by(deck_name=deck_name).first()
            if deck:
                return deck, 201
            else:
                abort(404,"Deck does not exist")
        else:
            deck = Deck.query.all()
            return deck,200

    @marshal_with(deck_fields)
    def post(self):
        deck_data = deck_post_parser.parse_args()

        deck = Deck.query.filter_by(deck_name=deck_data['deck_name']).first()
        user = User.query.filter_by(username = deck_data['username']).first()
        if deck:
            abort(404,"Deck already exists")
        else:
            #getting user id
            uid = user.user_id
            
            #get decks by current user
            decks = Deck.query.filter_by(deck_name = deck_data['deck_name']).all()   #get all decks with this name
            deck_foreign = UserDeckRelation.query.filter_by(userUCR_foreignid = uid).all()
            if deck_foreign: # if current user has created any decks
                if decks: # if there are any decks with this deck name 
                    for deck in decks:
                        for deck_ in deck_foreign:
                            if deck.deck_id == deck_.deckUCR_foreignid: #if user has created deck with deck name entered 
                                abort(409, "User has already created a deck with this name.")
           
            #creating deck
            new_deck_data = Deck(deck_name = deck_data['deck_name']) #Enter deck into deck table
            db.session.add(new_deck_data)
            db.session.commit()
            deck = Deck.query.filter_by(deck_name = deck_data['deck_name']).first()
            did = deck.deck_id
            deck_user_data = UserDeckRelation(userUCR_foreignid = uid, deckUCR_foreignid = did) #enter data into deck-user table
            db.session.add(deck_user_data)
            db.session.commit()
            return deck,200

    @marshal_with(deck_fields)
    def put(self, deck_name = None):
        if not deck_name:
            abort(400, "Deck name not specified")
        else:
            deck_data = deck_parser.parse_args()
            deck = Deck.query.filter_by(deck_name=deck_name).first()
            if deck is None:
                abort(404,"Deck does not exist")
            else:
                d_new = deck_data['deck_name']
                Deck.query.filter_by(deck_name = deck_name).update(dict(deck_name = d_new))
                db.session.commit()
                return deck,200
                

    @marshal_with(deck_fields)
    def delete(self, username, deck_name = None):
        if not deck_name:
            abort(400, "Deck Name not Specified")
        else:
            deck = Deck.query.filter_by(deck_name = deck_name).first()
            if deck:
                user = User.query.filter_by(username = username).first()
                uid = user.user_id
                did = deck.deck_id
                #delete deck from deck table
                deck = Deck.query.filter_by(deck_name = deck_name).delete() 
                db.session.commit()
                #delete deck user instance from UserDeckRelation 
                UserDeckRelation.query.filter_by(userUCR_foreignid = uid, deckUCR_foreignid = did).delete()
                db.session.commit()
                
                cards = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).all()
                #delete all cards of that deck
                for card in cards:
                    Card.query.filter_by(card_id = card.cardCDR_foreignid).delete()
                    db.session.commit()
                #delete cards in card deck relation
                cards = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).delete()
                db.session.commit()
                return "Deck Deleted Successfully", 200
            else:
                abort(404,"Deck does not exist")
        

class CardResource(Resource):
    @marshal_with(card_fields)
    def get(self, deck_name = None, card_front = None):
        if deck_name:
            deck = Deck.query.filter_by(deck_name=deck_name).first()
            if deck:
                return deck, 201
            else:
                abort(404,"Deck does not exist")
        else:
            deck = Deck.query.all()
            return deck,200