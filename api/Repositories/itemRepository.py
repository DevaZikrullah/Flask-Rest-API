from api import marshal_with,Blueprint,db,request
from api.models import Item,itemSerialized

itemRoute = Blueprint('item_route',__name__)

class ItemRepository:

    @itemRoute.route('/item',methods = ['GET'])
    @marshal_with(itemSerialized)
    def get():
        item = Item.query.all()
        return item


    def post(name):
        item  = Item(name = name)
        db.session.add(item)
        db.session.commit()
        return Item.query.all()

    def getByName(name):
        item = Item.query.filter_by(name=name).first()
        return item
    
