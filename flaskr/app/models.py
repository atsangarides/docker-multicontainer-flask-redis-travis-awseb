from app import db


class Values(db.Model):
    __tablename__ = "values"

    row_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
