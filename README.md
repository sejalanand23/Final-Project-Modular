# Flashcard Application

This is an application where users can create decks of flashcards and take quizzes on the same. The backend has been developed using flask and VueJS is being used to render the frontend. Flask RESTful API is working in the middle.

# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Start redis server
```
brew services start redis
```
## Celery Jobs
```
celery -A main.celery worker --loglevel=info
```

## Flask Application

### Install Requirements
```
pip install -r requirements.txt
```
### Running the Application
Run main.py


## Files and Folders Structure
- __Final Project Modular__
   - __backend__
     - __application__
       - [api.py](backend/application/api.py)
       - [config.py](backend/application/config.py)
       - [controllers.py](backend/application/controllers.py)
       - [database.py](backend/application/database.py)
       - [models.py](backend/application/models.py)
       - [security.py](backend/application/security.py)
       - [tasks.py](backend/application/tasks.py)
       - [validation.py](backend/application/validation.py)
       - [workers.py](backend/application/workers.py)
     - [celerybeat\-schedule.db](backend/celerybeat-schedule.db)
     - __db\_directory__
       - [ER diagram.png](backend/db_directory/ER%20diagram.png)
       - [database.sqlite3](backend/db_directory/database.sqlite3)
       - [database.sqlite3.sql](backend/db_directory/database.sqlite3.sql)
     - [main.py](backend/main.py)
     - [requirements.txt](backend/requirements.txt)
   - __frontend__
     - [README.md](frontend/README.md)
     - [babel.config.js](frontend/babel.config.js)
     - [jsconfig.json](frontend/jsconfig.json)
     - [node\_modules](frontend/node_modules)
     - [package\-lock.json](frontend/package-lock.json)
     - [package.json](frontend/package.json)
     - __public__
       - [favicon.ico](frontend/public/favicon.ico)
       - [index.html](frontend/public/index.html)
     - __src__
       - [App.vue](frontend/src/App.vue)
       - __assets__
         - [home.jpeg](frontend/src/assets/home.jpeg)
       - __components__
       - [main.js](frontend/src/main.js)
       - __router__
         - [index.js](frontend/src/router/index.js)
       - __views__
         - [AboutView.vue](frontend/src/views/AboutView.vue)
         - [AddCards.vue](frontend/src/views/AddCards.vue)
         - [CreateDeck.vue](frontend/src/views/CreateDeck.vue)
         - [DeckQuiz.vue](frontend/src/views/DeckQuiz.vue)
         - [EditCards.vue](frontend/src/views/EditCards.vue)
         - [EditDeck.vue](frontend/src/views/EditDeck.vue)
         - [HomeView.vue](frontend/src/views/HomeView.vue)
         - [Login.vue](frontend/src/views/Login.vue)
         - [Register.vue](frontend/src/views/Register.vue)
         - [UserDashboard.vue](frontend/src/views/UserDashboard.vue)
     - [vue.config.js](frontend/vue.config.js)
     - [yarn.lock](frontend/yarn.lock)