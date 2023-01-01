from api import marshal_with,Blueprint,db,request,jsonify,generate_password_hash,check_password_hash,jwt,app
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

    @userRoute.route('/login',methods =['POST'])
    def login():
        data = request.json
        user = User.query.filter_by(name=data['name']).first()

        if not user:
            return jsonify(
                message = "not found name",
                status = 404
            )

        if check_password_hash(user.password,data['password']):
            token = jwt.encode({
            'id': user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, app.config['SECRET_KEY'],algorithm="HS256")

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

        # def info_user():
