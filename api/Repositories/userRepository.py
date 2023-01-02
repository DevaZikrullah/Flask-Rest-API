from api import (marshal_with,
                    Blueprint,
                    db,
                    request,
                    jsonify,
                    generate_password_hash,
                    check_password_hash,
                    app,
                    jwt_required,
                    create_access_token,
                    get_jwt_identity
                    )
from api.models import User,userSerialized
from datetime import datetime, timedelta

userRoute = Blueprint('user_route',__name__)

class UserRepository:

    @userRoute.route('/users',methods =['GET'])
    @marshal_with(userSerialized)
    def get():
        users = User.query.all()
        return users    

    @userRoute.route('/users',methods =['POST'])
    @marshal_with(userSerialized)
    def post():
        data = request.json
        user  = User(
            name = data['name'],
            password = generate_password_hash(data['password']),
            point = data['point']
            )
        check = User.query.filter_by(name=data['name']).first()
        if not check:
            db.session.add(user)
            db.session.commit()
            return User.query.all()
        else:
            return 404
