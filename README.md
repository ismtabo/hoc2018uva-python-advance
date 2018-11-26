# Hour of code 2018 - Pybbo: Flask ♥️ Vuejs

This is a sample of a simple social network made in Python using Flask, Vue, Peewee and SocketIO made for the [Hour of Code 2018.](http://eventos.uva.es/27587/detail/la-hora-del-codigo-2018.html)

## How to follow this tutorial

First of all, download this repository to your machine:
```
$ git clone https://github.com/ismtabo/hoc2018uva-python-advance
```

Now choose how do you want to install the dependencies needed:

- Virtualenv: 
    - To install on Ubuntu based UNIX/Linux systems, execute this command:
        ```
        $ sudo apt install virtualenv
        ```
    - To install on Arch based UNIX/Linux systems, execute this command:
        ```
        $ pacman -S python-virtualenv
        ```
    - To install on other OS, follow the instructions at the official web page: https://virtualenv.pypa.io/en/stable/

- Pipenv:
	- To install with `pip`, execute the command bellow:
		```
		$ pip install pipenv
		```
	- If you want more information: https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv

## Tutorial content

This sample is dividen in three different parts:

1. Flask as a Web application:
    1. Prepare the virtual environment or install dependencies globally:
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
    3. Dynamic content generation with templates
    4. Comment structure using:
        - Templates
        - `collections.namedtuple`
    5. Listing comments
    6. Make a form to post comments
2. Real time web application:
	1. Update new comments in real time using SocketIO
	2. Post new comments without having to refresh the web page using Axios
3. Single page application using Vue.js:
	1. _Hello World_ using Vue.js
	2. Flask as a REST server
	3. Realtime web application made easier
4. Data persistence using Peewee:
    1. Comment class
    2. Create a SQLite database
    3. Adding a method to write comments into the database
    4. Adding a method to retrieve comments from the database
    5. Link the database with flask
5. Authentication:
	1. User and session management using Flask-Login
	2. Login and logout
	3. REST authentication using JWT
	4. Store the token using Vuex
6. Profile management:
	1. Extending the user class
	2. Change the user password
	3. Add an user bio
	4. Update profile information
7. Chat rooms:
	1. Chat page
	2. Join a room
	3. Chat messages
	4. Leave room


## Getting started into the tutorial

The tags below are used to identify the different tutorial steps, you can see them at: https://github.com/ismtabo/hoc2018uva-python-advance/releases

To jump between the tutorial parts, checkout the tag using the command below:
```
$ git checkout <tag_name>
```

For the first tag and the start of the tutorial, it would be this command:
```
$ git checkout v1.0-flask-hello-world
```

If you want to change the tag but you've made changes to the code, git won't let you checkout. You'll have to use the `--force` flag to discard your changes like this:
```
$ git checkout --force v1.1-flask-templates # Drop all my changes and go to the v1.1 tag
```

Contributors
---
- Ismael Taboada: [ismtabo](https://github.com/ismtabo)
- Carlos Gómez: [kurolox](https://github.com/kurolox)
