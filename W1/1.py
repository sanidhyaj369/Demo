from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/Flask_database'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(70), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    notes_id = db.Column(db.Integer, db.ForeignKey('notes.id'))

    def __repr__(self):   # representation method
        return f'<user> {self.firstname} {self.id}'
    

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user = db.relationship('User', backref="notes", lazy = True)

    def __repr__(self):
        return f'<Notes> {self.title}'