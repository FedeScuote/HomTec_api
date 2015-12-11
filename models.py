from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import validates

#
# class Result(db.Model):
#     __tablename__ = 'results'
#
#     id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.String())
#     result_all = db.Column(JSON)
#     result_no_stop_words = db.Column(JSON)
#
#     def __init__(self, url, result_all, result_no_stop_words):
#         self.url = url
#         self.result_all = result_all
#         self.result_no_stop_words = result_no_stop_words
#
#     def __repr__(self):
#         return '<id {}>'.format(self.id)
#

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    lastname = db.Column(db.String())
    ci = db.Column(db.Integer())
    email = db.String(db.String())

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address