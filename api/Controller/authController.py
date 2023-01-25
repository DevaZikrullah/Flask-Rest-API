from api import Blueprint,request,render_template
from api.Repositories.userRepository import *

authentication = Blueprint('auth_route',__name__)

class Authentication:
    @authentication.route('/register', methods =['GET', 'POST'])
    def register():
        username = request.form['username']
        password = request.form['password']
        point = request.form['point']
        data = {
            'username':username,
            'password':password,
            'point':point
        }
        if not UserRepository.getByName(username):
            UserRepository.post(data)
            return 
        else:
            return 
        
            
    @authentication.route('/index')
    def index():
        name = 'Rosalia'
        # username1 = request.form['username1']
    
        return render_template('index.html', title='Welcome')