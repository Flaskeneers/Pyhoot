# Pyhoot

## About

School-project on Web-framework.

Pyhoot is a quiz-application that will run through your browser using Flask.

Features:

- a login-system, and authentication.
- Create your own multiple-choice questions, and send them to your friends and let them take it.
- standard CRUD-features from database
- profile-pages linked to each user, containting that users created_quizzes


Planned features:
- SocketIO integration - users will be able to create lobbies and send an invite-link to friends in order to take a Quiz in realtime and compete against each other (Kahoot-style)
- quiz-page where the user can take a quiz and get a highscore


### UML Diagram

![UML diagram of the MongoDB documents in the project](assets/pyhoot_uml.png?raw=true "Pyhoot UML diagram")


## Setup

1. Install packages from requirements.txt
2. Add an environment file called `.env` in the projects root directory with values set for these following keys:

> .env

    # Flask
    SECRET_KEY=...

    # DB
    MONGO_DB_NAME=database-name
    MONGO_DB_PROTOCOL=mongodb
    MONGO_DB_USER=root
    MONGO_DB_PASS=super-secret-password
    MONGO_DB_HOST=localhost
    MONGO_DB_PORT=27017  # 27017 by default or something like 27020 if it does not work
    
    # Mail 
    # (Example is for gmail, you will need to enable 'Less secure app access' in your Google settings)
    MAIL_SERVER=smtp.gmail.com
    MAIL_USERNAME=jane.doe@gmail.com
    MAIL_PASSWORD=super-secret-password
    MAIL_USE_TLS=True
    MAIL_SENDER=jane.doe@gmail.com
    MAIL_PORT=587