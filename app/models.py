from app import db


class User(db.Model):
    id = db.Column(db.Integerm primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(sb.String(120), index=True, unique=True)
    password_hash = db.Column(db.string(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
