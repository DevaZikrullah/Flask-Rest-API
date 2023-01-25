from api import (marshal_with,
                    Blueprint,
                    db,
                    request,
                    generate_password_hash
                    )
from api.models import User,userSerialized

userRoute = Blueprint('user_route',__name__)

class UserRepository:

    # @userRoute.route('/users',methods =['GET'])
    # @marshal_with(userSerialized)
    def get():
        users = User.query.all()
        return users    

    def post(data):
        user  = User(
            name = data['username'],
            password = generate_password_hash(data['password']),
            point = data['point']
            )
        
        check = UserRepository.getByName(data['username'])
        if not check:
            db.session.add(user)
            db.session.commit()
            return User.query.all()
        else:
            raise Exception('data sudah ada')
        
    def getByName(username):
        user =  User.query.filter_by(name=username).first()
        return user
