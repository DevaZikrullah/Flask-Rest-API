from api import app,request,db,marshal_with
from .models import Item,itemSerialized
from .Repositories.itemRepository import itemRoute
from .Repositories.userRepository import userRoute
from .Domain.auth import auth

app.register_blueprint(itemRoute)
app.register_blueprint(userRoute)
app.register_blueprint(auth)
