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


## Backend

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
       - [validation.py](backend/application/validation.py)
     - __db\_directory__
       - [database.sqlite3](backend/db_directory/database.sqlite3)
       - [database.sqlite3.sql](backend/db_directory/database.sqlite3.sql)
     - [main.py](backend/main.py)
     - __static__
       - [home.jpeg](backend/static/home.jpeg)
     - __templates__
       - [add\_cards.html](backend/templates/add_cards.html)
       - [create\_deck.html](backend/templates/create_deck.html)
       - [dashboard.html](backend/templates/dashboard.html)
       - [edit\_deck.html](backend/templates/edit_deck.html)
       - [home.html](backend/templates/home.html)
       - [login.html](backend/templates/login.html)
       - [quiz.html](backend/templates/quiz.html)
       - [quiz\_ans.html](backend/templates/quiz_ans.html)
       - [register.html](backend/templates/register.html)
       - [result.html](backend/templates/result.html)
       - __security__
         - [\_messages.html](backend/templates/security/_messages.html)
         - [base.html](backend/templates/security/base.html)
         - [login\_user.html](backend/templates/security/login_user.html)
         - [register\_user.html](backend/templates/security/register_user.html)
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
         - [logo.png](frontend/src/assets/logo.png)
       - __components__
         - [HelloWorld.vue](frontend/src/components/HelloWorld.vue)
       - [main.js](frontend/src/main.js)
       - __router__
         - [index.js](frontend/src/router/index.js)
       - __views__
         - [AboutView.vue](frontend/src/views/AboutView.vue)
         - [Dashboard.vue](frontend/src/views/Dashboard.vue)
         - [HomeView.vue](frontend/src/views/HomeView.vue)
         - [Login.vue](frontend/src/views/Login.vue)
         - [Register.vue](frontend/src/views/Register.vue)
     - [vue.config.js](frontend/vue.config.js)
   - [requirements.txt](requirements.txt)

