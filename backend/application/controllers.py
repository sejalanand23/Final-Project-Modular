from flask import Flask
from flask import render_template, redirect,request,flash,url_for,session,jsonify
from flask_restful import Api,Resource,fields,marshal_with,reqparse,abort
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from application.security import user_datastore, sec
# from flask_security import hash_password
from flask import current_app as app
from application.models import *
from application.validation import *
import time


@app.route('/')
def home():
  return render_template('home.html')
  # return "API call successful"

@app.route('/register',methods = ['GET','POST'])
def register():
  if request.method == 'POST':
    uname = request.form['email']
    pswd = request.form['password'] 

    user = User.query.filter_by(email = uname).first()

    if user:
      flash('email already exists. Try with a different email')
      return redirect((url_for('register')))
      # response = jsonify({'message' : 'email already exists'})
      # response.status_code = 409
      # return response
    else:
      u = User(email = uname,password = pswd)
      db.session.add(u)
      db.session.commit()
      flash('Account Created Successfully. Login to continue.')
      return redirect((url_for('login')))
      # response = jsonify({'message' : 'Account Created Successfully!'})
      # response.status_code = 200
      # return response
  return render_template('register.html')

@app.route('/login',methods = ['GET','POST'])
def login():
  if request.method == "POST":
    session['uname'] = request.form['email']
    session['pswd'] = request.form['password'] 

    user = User.query.filter_by(email = session['uname']).first()
    if not user:
      flash('User does not exist.')
      return redirect((url_for('login')))
      # response = jsonify({'message' : 'User does not exist'})
      # response.status_code = 404
      # return response

    else:
      p = user.password
      user_name = user.email
      if session['pswd'] == p:
        url = '/dashboard/'+str(user_name)
        return redirect(url)
        # response = jsonify({'message' : 'You are logged in successfully'})
        # response.status_code = 200
        # return response
      else:
        flash('Password incorrect.Try again!')
        # response = jsonify({'message' : 'Password incorrect'})
        # response.status_code = 401
        # return response
      
  return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session['user'] = None
    return redirect(url_for('home'))

@app.route('/dashboard/<string:user_name>',methods = ['GET','POST'])
def dashboard(user_name):
  user = User.query.filter_by(email = user_name).first()
  uid = user.id
  decks = Deck.query.all()
  score_info = UserDeckRelation.query.all()
  session['ques_seen'] = 0
  return render_template('dashboard.html',user_name = user_name, decks = decks,score_info = score_info,uid = uid) 

@app.route('/dashboard/<string:user_name>/createdeck',methods = ['GET','POST'])
def create_deck(user_name):
  user = User.query.filter_by(email = user_name).first()
  uid = user.id
  if request.method == 'POST':
    deck_name = request.form['deck_name']
    decks = Deck.query.filter_by(deck_name = deck_name).all()   #get all decks with this name
    deck_foreign = UserDeckRelation.query.filter_by(userUCR_foreignid = uid).all() #get decks by current user
    if deck_foreign: # if current user has created any decks
      if decks: # if there are any decks with this deck name 
        for deck in decks:
          for deck_ in deck_foreign:
            if deck.deck_id == deck_.deckUCR_foreignid: #if user has created deck with deck name entered
              flash('You have already create a deck with this name!')
              url = '/dashboard/'+str(user_name)+'/'+'createdeck'
              return redirect(url)
    deck_data = Deck(deck_name = deck_name) #Enter deck into deck table
    db.session.add(deck_data)
    db.session.commit()
    did = deck_data.deck_id
    # deck = Deck.query.filter_by(deck_name = deck_name).all()
    # did = deck.deck_id
    deck_user_data = UserDeckRelation(userUCR_foreignid = uid, deckUCR_foreignid = did) #enter data into deck-user table
    db.session.add(deck_user_data)
    db.session.commit()
    flash('Deck Created Successfully!')
    url = '/dashboard/'+str(user_name)+'/'+str(deck_name)+'/addcards'
    return redirect(url)
  return render_template('create_deck.html',user_name = user_name)

@app.route('/dashboard/<string:user_name>/<string:deck_name>/editdeck',methods = ['GET','POST'])
def edit_deck(user_name, deck_name):
  if request.method == 'POST':
    d_new = request.form['deck_name_new']
    Deck.query.filter_by(deck_name = deck_name).update(dict(deck_name = d_new))
    db.session.commit()
    url = '/dashboard/'+str(user_name)
    return redirect(url)
  return render_template('edit_deck.html',user_name = user_name, deck_name = deck_name)

@app.route('/dashboard/<string:user_name>/<string:deck_name>/delete_deck',methods = ['GET','POST'])
def delete_deck(user_name, deck_name):
  user = User.query.filter_by(email = user_name).first()
  uid = user.id
  deck = Deck.query.filter_by(deck_name = deck_name).first()
  did = deck.deck_id
  deck = Deck.query.filter_by(deck_name = deck_name).delete()
  db.session.commit()
  UserDeckRelation.query.filter_by(userUCR_foreignid = uid, deckUCR_foreignid = did).delete()
  db.session.commit()
  cards = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).all()
  for card in cards:
    Card.query.filter_by(card_id = card.cardCDR_foreignid).delete()
    db.session.commit()
  cards = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).delete()
  db.session.commit()
  url = '/dashboard/'+str(user_name)
  return redirect(url)
  

@app.route('/dashboard/<string:user_name>/<string:deck_name>/addcards',methods = ['GET','POST'])
def add_cards(user_name,deck_name):
  if request.method == 'POST':
    front = request.form['card_front']
    back = request.form['card_back']
    card_data = Card(card_front = front, card_back = back)
    db.session.add(card_data)
    db.session.commit()
    card_info = Card.query.filter_by(card_front = front).first()
    cid = card_info.card_id
    deck = Deck.query.filter_by(deck_name = deck_name).first()
    did = deck.deck_id
    card_deck_data = CardDeckRelation(cardCDR_foreignid = cid,deckCDR_foreignid = did)
    db.session.add(card_deck_data)
    db.session.commit()
    flash('Card Added Successfully! Add Another.')
    url = '/dashboard/'+str(user_name)+'/'+str(deck_name)+'/addcards'
    return redirect(url)
  return render_template('add_cards.html',user_name = user_name, deck_name = deck_name)

@app.route('/dashboard/<string:user_name>/<string:deck_name>/quiz',methods = ['GET','POST'])
def quiz(user_name, deck_name):
  
  deck = Deck.query.filter_by(deck_name=deck_name).first()
  did = deck.deck_id
  cards_relation = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).all()

  cards_frontback = dict() #dict to store cards front and back
  cards_difficulty = dict()

  for card_relation in cards_relation:
    c_fid = card_relation.cardCDR_foreignid
    card = Card.query.filter_by(card_id = c_fid).first()
    cards_frontback[card.card_front] = card.card_back
    cards_difficulty[card.card_front] = None


  global n
  n = len(cards_frontback)

  # session['index'] = random.randint(0,n-1)
  # index = session['index']

  session['ques_seen']

  if session['ques_seen'] == n:
    review_time = time.ctime()

    deck = Deck.query.filter_by(deck_name=deck_name).first() #get deck id
    did = deck.deck_id
    deck_user_data = UserDeckRelation.query.filter_by(deckUCR_foreignid = did).first()
    out_of = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).count()
    if not deck_user_data.quiz_count:
      deck_user_data.quiz_count = 1
      deck.deck_total_score = deck_user_data.correct
      deck.deck_average_score = deck.deck_total_score / out_of
    else:
      deck_user_data.quiz_count += 1
      if not deck.deck_total_score:
        deck.deck_total_score = deck_user_data.correct
      else:
        deck.deck_total_score += deck_user_data.correct
      deck.deck_average_score = deck.deck_total_score / out_of

    deck_user_data.time = review_time
    db.session.commit()

    url = '/dashboard/'+str(user_name)+'/'+str(deck_name)+'/result'
    return redirect(url)

  keys = list(cards_frontback.keys())
  card_front = keys[session['ques_seen']]
  card_back = cards_frontback[card_front]
  session['ques_seen'] += 1
  

  return render_template('quiz.html',user_name = user_name, deck_name = deck_name, cards_frontback = cards_frontback, \
    cards_difficulty = cards_difficulty, card_front = card_front,card_back = card_back )

@app.route('/dashboard/<string:user_name>/<string:deck_name>/quiz_ans',methods = ['GET','POST'])
def quiz_ans(user_name,deck_name):
  if request.method == 'POST':
    card_front = request.form.get("card_front")
    card_back = request.form.get("card_back")
    answer = request.form['ans']
    difficulty = request.form['difficulty']
    deck = Deck.query.filter_by(deck_name=deck_name).first() #get deck id
    did = deck.deck_id
    deck_score_data = UserDeckRelation.query.filter_by(deckUCR_foreignid = did).first() #get corresponding user deck info

    card = Card.query.filter_by(card_front = card_front).first() #get card
    card.difficulty = difficulty #enter card difficulty in db
    db.session.commit()
    #update score
    ques_seen = session.get('ques_seen')

    answer = answer.strip()
    
    if ques_seen == 1:
      if answer.lower() == card.card_back.lower():
        deck_score_data.correct = 1
      else:
        deck_score_data.correct = 0
    else:
      if answer.lower() == card.card_back.lower():
        deck_score_data.correct += 1
    db.session.commit()

  deck = Deck.query.filter_by(deck_name=deck_name).first()
  did = deck.deck_id
  cards_relation = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).all()
  cards_frontback = dict() #dict to store cards front and back
  cards_difficulty = dict()
  for card_relation in cards_relation:
    c_fid = card_relation.cardCDR_foreignid
    card = Card.query.filter_by(card_id = c_fid).first()
    cards_frontback[card.card_front] = card.card_back
    cards_difficulty[card.card_front] = None
  # n = len(cards_frontback)
  # card_front = next(iter(cards_frontback))
  # card_back = cards_frontback[card_front]
  return render_template('quiz_ans.html',user_name = user_name, deck_name = deck_name,cards_frontback = cards_frontback, \
    card_front = card_front, card_back = card_back )

@app.route('/dashboard/<string:user_name>/<string:deck_name>/result',methods = ['GET','POST'])
def result(user_name,deck_name):
  deck = Deck.query.filter_by(deck_name=deck_name).first() #get deck id
  did = deck.deck_id
  deck_user_data = UserDeckRelation.query.filter_by(deckUCR_foreignid = did).first()
  score = deck_user_data.correct
  out_of = CardDeckRelation.query.filter_by(deckCDR_foreignid = did).count()
  
  return jsonify({"Score":score, "Out_of":out_of})
  # return render_template('result.html',user_name = user_name, deck_name = deck_name, score = score, out_of = out_of)