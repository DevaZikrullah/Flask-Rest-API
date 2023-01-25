from api import db,fields

itemSerialized = {
    'id':fields.Integer,
    'name':fields.String
}

class Item(db.Model):
    __tablename_ = 'item'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name
    
    

userSerialized = {
    'id':fields.Integer,
    'name':fields.String,
    'password':fields.String,
    'point':fields.Integer
}

class User(db.Model):
    __tablename_ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(225),nullable = False)
    point = db.Column(db.Integer, nullable = False)
    activated = db.Column(db.String(20))

    def __init__(self,name,password,point):
        self.name = name
        self.password = password
        self.point = point 

    def __repr__(self):
        return self.name
    
    
