from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)
    userType = db.Column(db.String(50))
    web3Address = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.id} - {self.username}"
    
class PendingRequests(db.Model):
    req_id = db.Column(db.Integer, primary_key=True)
    req_from  = db.Column(db.String(50))
    productName = db.Column(db.String(30))
    numOfItem = db.Column(db.Integer)
    to_id = db.Column(db.Integer)
    web3Address_from = db.Column(db.String(100))
    message = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.req_from} - {self.message} - {self.to_id}"
