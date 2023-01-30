from api import (marshal_with,
                    Blueprint,
                    db,
                    request,
                    generate_password_hash
                    )
from api.models import User,userSerialized

userRoute = Blueprint('user_route',__name__)

class UserRepository:

    def get():
        users = User.query.all()
        return users    

    def post(username,password,point):
        user  = User(username,password,point)
        return User.query.all()
        
    def getByName(username):
        user =  User.query.filter_by(name=username).first()
        return user
