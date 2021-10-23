# Music Streamer application

This is a collaborative project, meant to model a real time music streaming application using the Django Rest Framework. 

#PS: This project is still ongoing and yet to be completed

## How the project is structured
We placed the various apps in a dedicated app folder for easy workflow.
One app for songs and albums, another one for reviews of songs and albums, and the third one 
for user accounts. 

The database used is Amazon's AWS S3 for media storage and the default sqlite for everything else.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/hengage/music-streamer-API.git

$ cd music-streamer
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv <name_of_env>
$ env/Scripts/activate (Windows)
$ source env/bin/activate (Mac)
OR
$ python3 -m venv <name_of_env>
$ <name_of_env>\Scripts\activate (Windows)
$ source <name_of_env>/bin/activate
```

Then install the dependencies:

```sh
(<name_of_env>)$ pip install -r requirements.txt
```
Note the `(<name_of_env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by virtualenv or venv.

Once `pip` has finished downloading the dependencies:
```sh

(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/`.


## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test musicstreamer_app
```
