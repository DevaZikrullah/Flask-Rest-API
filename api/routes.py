from api import app,Blueprint
from .models import Item,itemSerialized
from .Repositories.itemRepository import itemRoute
from .Repositories.userRepository import userRoute
from .Domain.authDomain import authRoute
from .Controller.authController import authentication
from .Controller.itemController import itemRouteController

api = Blueprint('api', __name__, url_prefix='/api')
web = Blueprint('web',__name__)

api.register_blueprint(itemRoute)
api.register_blueprint(userRoute)
api.register_blueprint(authRoute)
api.register_blueprint(itemRouteController)

app.register_blueprint(api)

web.register_blueprint(authentication)

app.register_blueprint(web)