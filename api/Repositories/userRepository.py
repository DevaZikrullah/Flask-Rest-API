from api import marshal_with,Blueprint,db,request,jsonify
from api.models import User,userSerialized

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
        user  = User(name = data['name'],password = data['password'],point = data['point'])
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
                message = "not found id",
                status = 404
            )

        if user.password != data['password']:
            return jsonify(
                message = "wrong password",
                status = 401
            )

        return jsonify(
            message = "Login Succsesfull",
            status = 201
        )