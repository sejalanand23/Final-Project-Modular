from turtle import back
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
# user_parser.add_argument('id',type=int)
user_parser.add_argument('email',type = str,required = True)
user_parser.add_argument('password',type = str)

deck_post_parser = reqparse.RequestParser()
deck_post_parser.add_argument('email',type = str,required = True)
deck_post_parser.add_argument('deck_name',type = str, required = True)

card_parser = reqparse.RequestParser()
# card_parser.add_argument('card_id',db.Integer)
card_parser.add_argument('card_front',type = str)
card_parser.add_argument('card_back',type = str)
card_parser.add_argument('difficulty',type = str)

card_post_parser = reqparse.RequestParser()
card_post_parser.add_argument('email',type = str,required = True, help = "User is Required")
card_post_parser.add_argument('card_front',type = str,required = True, help = "Card Front is Required")
card_post_parser.add_argument('card_back',type = str,required = True, help = "Card Back is Required")
card_post_parser.add_argument('deck_id',type = int, required = True, help = "Deck Info is Required")

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
    def get(self,email=None):
        if email:
            user = User.query.filter_by(email = email).first()
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
        user = User.query.filter_by(email = user_args['email']).first()
        if user:
            abort(409,"User already exists")
        else:
            u = User(email = user_args['email'],password = user_args['password'])
            db.session.add(u)
            db.session.commit()
            return u, 201


class DeckResource(Resource):
    @marshal_with(deck_fields)
    @auth_required("token")
    def get(self,email,deck_name):
        user = User.query.filter_by(email = email).first()
        if not user:
            abort(404, "User does not exist")
        else:
            uid = user.id     
            #get decks by current user
            decks = Deck.query.filter_by(deck_name = deck_name, ).all()   #get all decks with this name
            deck_foreign = UserDeckRelation.query.filter_by(userUCR_foreignid = uid).all()
            if deck_foreign: # if current user has created any decks
                if decks: # if there are any decks with this deck name 
                    for deck in decks:
                        for deck_ in deck_foreign:
                            if deck.deck_id == deck_.deckUCR_foreignid: #if user has created deck with deck name entered 
                                return deck,200
            abort(404,"Deck Not Found")
                    

    @marshal_with(deck_fields)
    @auth_required("token")
    def post(self):
        deck_data = deck_post_parser.parse_args()
        user = User.query.filter_by(email = deck_data['email']).first()
        if not user:
            abort(404, "User does not exist")
        else:
            uid = user.id      
        #get decks by current user
        decks = Deck.query.filter_by(deck_name = deck_data['deck_name'], ).all()   #get all decks with this name
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
        did = new_deck_data.deck_id
        deck_user_data = UserDeckRelation(userUCR_foreignid = uid, deckUCR_foreignid = did) #enter data into deck-user table
        db.session.add(deck_user_data)
        db.session.commit()
        return new_deck_data,200

    # @marshal_with(deck_fields)
    @auth_required("token")
    def put(self, deck_name = None):
        if not deck_name:
            abort(400, "Old Deck name not specified")
        else:
            deck_data = deck_post_parser.parse_args()
            email = deck_data['email']
            user = User.query.filter_by(email = email).first()
            uid = user.id
            decks = Deck.query.filter_by(deck_name = deck_name).all()
            for deck in decks:
                did = deck.deck_id
                deck_info = UserDeckRelation.query.filter_by(userUCR_foreignid = uid, deckUCR_foreignid = did).first()
                if deck_info:
                    d_new = deck_data['deck_name']
                    deck_to_update = Deck.query.filter_by(deck_id = did).first()
                    deck_to_update.deck_name = d_new
                    db.session.merge(deck_to_update)
                    db.session.commit()
                    return "Deck Name Updated Successfully",200
            abort(404,"User has no deck with this name.")
                

    # @marshal_with(deck_fields)
    @auth_required("token")
    def delete(self):    
            deck_data = deck_post_parser.parse_args()
            email = deck_data['email']
            user = User.query.filter_by(email = email).first()
            uid = user.id
            deck_name = deck_data['deck_name']
            decks = Deck.query.filter_by(deck_name = deck_name).all()
            for deck in decks:
                did = deck.deck_id
                deck_info = UserDeckRelation.query.filter_by(userUCR_foreignid = uid, deckUCR_foreignid = did).first()
                if deck_info:
                    deck_to_delete = db.session.query(Deck).filter_by(deck_id = did).first()
                    db.session.delete(deck_to_delete)
                    cards = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).all()
                    for card in cards:
                        card_to_delete = db.session.query(Card).filter_by(card_id = card.cardCDR_foreignid).first()
                        db.session.delete(card_to_delete)
                        db.session.commit()
                    return "Deck Deleted Successfully", 200
            else:
                abort(404,"Deck Not Found")
        

class CardResource(Resource):
    @marshal_with(card_fields)
    @auth_required("token")
    def get(self,card_id = None):
        card = Card.query.filter_by(card_id = card_id).first()
        if card:
            return card,200
        else:
            abort(404,"Card Not Found")
    
    # @marshal_with(card_fields)
    @auth_required("token")
    def put(self,card_id):
        card = Card.query.filter_by(card_id = card_id).first()
        if not card:
            abort(404, "Card Not Found")

        card_args = card_parser.parse_args()
        front_update = card_args.get('card_front', None)
        back_update = card_args.get('card_back', None)
        difficulty_update = (card_args.get('difficulty',None) or "easy")

        if not front_update:
            abort(400, "Card Front Not Specified")
        elif not back_update:
             abort(400, "Card Back Not Specified")
        else:    
            card.card_front = front_update
            card.card_back = back_update
            card.difficulty = difficulty_update
            db.session.merge(card)
            db.session.commit()
            return "Card updated successfully",200

    @marshal_with(card_fields)
    @auth_required("token")
    def post(self):
        card_args = card_post_parser.parse_args()

        user = User.query.filter_by(email = card_args['email']).first()
        if not user:
            abort(404, "User does not exist")
        else:     
            deck_info = UserDeckRelation.query.filter_by(userUCR_foreignid = user.id, deckUCR_foreignid = card_args['deck_id']).first()
            if not deck_info:
                abort(404, "User has no such deck")
            else:
                cards_in_deck = CardDeckRelation.query.filter_by(deckCDR_foreignid = deck_info.deckUCR_foreignid).all()
                for card in cards_in_deck:
                    card = Card.query.filter_by(card_front = card_args.card_front).first()
                    if card:
                        abort(409, "Card already exists")
                    else:
                        new_card = Card(card_front = card_args.card_front, card_back = card_args.card_back)
                        db.session.add(new_card)
                        db.session.commit()
                        cid = new_card.card_id
                        card_deck_info = CardDeckRelation(cardCDR_foreignid = cid, deckCDR_foreignid = deck_info.deckUCR_foreignid)
                        db.session.add(card_deck_info)
                        db.session.commit()
                        return "Card added successfully", 200
         
    @auth_required("token")
    def delete(self,card_id):
        card = db.session.query(Card).filter_by(card_id = card_id).first()
        if card:
            db.session.delete(card)
            db.session.commit()
            return "Card Deleted Succesfully",200
        else:
            abort(404,"Card Not Found")

class QuizResource(Resource):
    @marshal_with(card_fields)
    @auth_required("token")
    def get(self,email,deck_name):
        user = User.query.filter_by(email = email).first()
        if not user:
            abort(404, "User does not exist")
        else:
            uid = user.id     
            #get decks by current user
            decks = Deck.query.filter_by(deck_name = deck_name, ).all()   #get all decks with this name
            deck_foreign = UserDeckRelation.query.filter_by(userUCR_foreignid = uid).all()
            if deck_foreign: # if current user has created any decks
                if decks: # if there are any decks with this deck name 
                    for deck in decks:
                        for deck_ in deck_foreign:
                            if deck.deck_id == deck_.deckUCR_foreignid: #if user has created deck with deck name entered 
                                all_card_ids = db.session.query(CardDeckRelation).with_entities(CardDeckRelation.cardCDR_foreignid).filter(CardDeckRelation.deckCDR_foreignid == deck.deck_id).all()
                                ids = [id for (id,) in all_card_ids]
                                cards = db.session.query(Card).filter(Card.card_id.in_(ids)).all()
                                return cards,200

            abort(404,"Deck Not Found")
