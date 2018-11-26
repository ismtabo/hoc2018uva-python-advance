# Hour of code 2018 - Pybbo: Flask ♥️ Vuejs

Sample of simple web service using Python3 with Flask, Peewee and Telepot for Hour of Code of 2017.

## How to follow this tutorial

First of all, download at your machine:
```
$ git clone https://github.com/ismtabo/hoc2018uva-python-advance
```

Choose your way to handle the dependencies:
- Virtualenv: 
    - To install on UNIX/Linux systems, execute below command:
        ```
        $ sudo apt install virtualenv
        ```
    - To install on other OS, follow instructions at official web page: https://virtualenv.pypa.io/en/stable/
- Pipenv:
	- To install with `pip`, execute command bellow:
		```
		$ pip install pipenv
		```
	- More information: https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv

## Contents of tutorial

Sample has three different parts:

1. Flask as Web application:
    1. Prepare virtual environment or use global system:
		1. Using pip:
			```
			$ pip install -r requirements.txt # Use pip3
			$ python <command>                # Use python3
			```
		2. Using virtualenv:
			```
			$ virtualenv -p python3 venv
			$ source venv/bin/activate
			(venv) $ pip install -r requirements.txt
			```
		3. Using pipenv:
			```
			$ pipenv install -r requirements.txt
			$ pipenv run <command>
			$ pipenv shell
			(venv) $ <command>
			```
    2. _Hello World_ using Flask
    3. Dynamic content generation with templates.
    4. Comment structure using:
        - Templates
        - `collections.namedtuple`
    5. List of comments
    6. Form to post comments
2. Realtime web application:
	1. Update content comments in realtime using Socketio
	2. Post new comments without refresh the web page using Axios
3. Single page application using Vuejs:
	1. _Hello World_ using Vuejs
	2. Flask as REST server
	3. Realtime web application much easier
4. Persistence using Peewee:
    1. Comment class
    2. Create database of SQLite
    3. Add method to write comments into database
    4. Add method to retrieve comments from database
    5. Link database with flask
5. Authentication:
	2. User and session management using Flask-Login
	1. Login and logout
	3. REST authentication using JWT
	4. Store token using Vuex
6. Profile management:
	1. Extending user class
	2. Change password
	3. Add user bio
	4. Update profile infor
7. Chat rooms:
	1. Chat page
	2. Join room
	3. Chat messages
	4. Leave room


## Getting started into the tutorial

Below tags identify several steps of the tutorial, you can show them at: https://github.com/ismtabo/hoc2017uva-python3/releases

To start with the tutorial, checkout first one with below command:
```
$ git checkout <tag_name>
```

For first step, it will be:
```
$ git checkout v1.0-flask-hello-world
```

In case, you want to advance in the tutorial but you already have done changes in the code, first discard this changes with:
```
$ git stash save --keep-index # Add changes to stash
$ git stash drop              # Discard stash
```
And then, checkout correct step's tag.


Contributors
---
- Ismael Taboada: [ismtabo](https://github.com/ismtabo)
- Carlos Gómez: [kurolox](https://github.com/kurolox)
