from api.Domain.itemDomain import *
from api import request,jsonify

itemRouteController = Blueprint('item_route_controller',__name__)

class ItemController:
    
    @itemRouteController.route('/create-item',methods = ['POST'])
    def create():
        name = request.json['name']
        try:
            ItemDomain.createItem(name)
            return jsonify(
            status = 200,
            message = 'create item sucsess',
            )
        except:
            return jsonify(
                status=500,
                message = 'cant create item'
            )