# Flasky
This repository contains my code for the [Flask Web Development, 2nd Edition](https://www.amazon.com/Flask-Web-Development-Developing-Applications/dp/1449372627) book.

Flasky is a [Flask](http://flask.pocoo.org/) social blogging application web application in which authenticated users can follow\unfollow each other, as well as creating and editing their own blog posts and comments.

### Prerequisites:
The application was built using [Python 3.7](https://www.python.org/downloads/), so you should ensure you have it installed on your machine.

You can find the application requirements in the [requirements folder](https://github.com/Mohllal/flasky/tree/master/requirements).

### Features:
- Users registration and logging in subsystem.
- Users profiles and avatars using the [Gravatar service](https://en.gravatar.com/).
- Users follow\unfollow subsystem.
- Markdown support for blog posts.
- Comments moderation.
- Secure against Cross-Site Request Forgery (CSRF) attacks.
- Responsive and elegant UI.
- RESTful API endpoints.
- Unit tests.
- Database migrations.

### Usage:
1. Clone this repository to your desktop, go to the ```flasky``` directory and create a new virtual environment to create isolated Python environment.
**Note: I highly recommend using [Virtualenv](https://virtualenv.pypa.io/en/latest/).**

2. Install the application requirements:
```python
pip install -r requirements\dev.txt
```

2. Create these environnement variables:
**Note: MAIL_USERNAME and MAIL_PASSWORD environnement variables are necessary for sending confirmation emails to the newly registered users.**
```python
set FLASK_APP=run.py
set MAIL_USERNAME=<your-gmail-email-address>
set MAIL_PASSWORD=<your-gmail-password>
```

3. Run the CLI ```deploy```command to create the database:
```python
flask deploy
```
4. If you want to populate the database with some dummy data type:
```python
flask shell
>>> from app.fake import users, posts, follows, comments
>>> users()
>>> posts()
>>> follows()
>>> comments()
```
5. Run the application and go to [localhost:5000](http://127.0.0.1:5000/) to see the application running:
```python
flask run
```

6. You can run the unit tests using the CLI ```test```command:
```python
flask test
```

### License:
This software is licensed under the [MIT License](https://opensource.org/licenses/MIT).
