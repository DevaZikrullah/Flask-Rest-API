from api import (Blueprint,
                    request,
                    render_template,
                    jsonify,
                    check_password_hash,
                    jwt_required,
                    create_access_token,
                    get_jwt_identity
                    )
from api.models import User
from api.Repositories.userRepository import *


authRoute = Blueprint('auth_route',__name__)


class AuthDomain:
    def login(username,password):
        user = UserRepository.getByName(username)

        if not user:
           raise Exception('not found user')

        if check_password_hash(user.password,password):
            return 'Sucsess Login'
        else:
            raise Exception('Wrong Password')

    def info_my_acc(username):
        user = UserRepository.getByName(username)
        if not user:
            raise Exception('Username Not Found')
            
        return jsonify(
            name = user.name,
            password = user.password,
            point = user.point
        )
    
    def createAccount(username,password,point):
        if not UserRepository.getByName(username):
            raise Exception('username already taken')
        else:
            UserRepository.post(username,password,point)
            return 'succes create account'