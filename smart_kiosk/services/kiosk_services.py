import uuid


def place_order(inventory: list, item_id : str, quantity: int, orders: list):
    
    item = find_inventory_item_by_item_id(inventory, item_id)
    
    if item:
        if item['stock'] >= quantity:
            item['stock'] = item['stock'] - quantity
            total_cost = item['unit_price'] * quantity
            new_order = {
                "order_id" : str(uuid.uuid4()),
                "item_id" : item_id,
                "quantity" : quantity,
                "status" : "placed",
                "total_cost" : total_cost
            }
            orders.appened(new_order)
            return new_order
            
def find_inventory_item_by_item_id(invetory: list, item_id : str):
    for item in invetory:
        if item['id'] == item_id:
            return item
    
    return None

def update_order_status():
    pass

def cancel_order():
    pass

def count_orders_by_item_id():
    pass