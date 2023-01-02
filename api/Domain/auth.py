from api import (Blueprint,
                    request,
                    jsonify,
                    check_password_hash,
                    jwt_required,
                    create_access_token,
                    get_jwt_identity
                    )
from api.models import User


auth = Blueprint('auth_route',__name__)


class Auth:
    @auth.route('/login',methods =['POST'])
    def login():
        data = request.json
        user = User.query.filter_by(name=data['name']).first()

        if not user:
            return jsonify(
                message = "not found name",
                status = 404
            )

        if check_password_hash(user.password,data['password']):
            token = create_access_token(identity=user.name)

            return jsonify(
                # token = jwt.decode(token,app.config['SECRET_KEY'], algorithms="HS256"),
                bearer_token= token,
                message = "Login Succsesfull",
                status = 201
            )

        return jsonify(
            message = "wrong password",
            status = 401
        )

    @auth.route('/info',methods =['GET'])
    @jwt_required()
    def info_my_acc():
        user = User.query.filter_by(name = get_jwt_identity()).first()
        return jsonify(
            name = user.name,
            password = user.password,
            point = user.point
        )