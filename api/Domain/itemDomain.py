from api.Repositories.itemRepository import *

class ItemDomain:

    def createItem(name):
        if ItemRepository.getByName(name):
            raise Exception('name already exsist')
        else:    
            return ItemRepository.post(name)
