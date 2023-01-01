from api import marshal_with,Blueprint,db,request
from api.models import Item,itemSerialized

itemRoute = Blueprint('item_route',__name__)

class ItemRepository:

    @itemRoute.route('/item',methods = ['GET'])
    @marshal_with(itemSerialized)
    def get():
        item = Item.query.all()
        return item


    @itemRoute.route('/item',methods =['POST'])
    @marshal_with(itemSerialized)
    def post():
        data = request.json
        # item  = Item(id = data['id'],name = data['name'])
        item  = Item(name = data['name'])
        db.session.add(item)
        db.session.commit()
        return Item.query.all()
    
