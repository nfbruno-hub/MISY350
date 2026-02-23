
##List dictionaries
inventory = [
        {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
        {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
        {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
        {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
        {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18}
]

Orders = [
        {"Order iD": "Order_101", "Item ID": 2, "Quantity": 2, "Status": "Placed", "Total": 8.50},
        {"Order iD": "Order_102", "Item ID": 3, "Quantity": 1, "Status": "Placed", "Total": 3.75}
]


##CRUD

#Query 0: View all items in the inventory with stock less than 20.

#Input:
#Define the threshold for low stock and access the inventory list.
threshold = 5

#Process: Find items with stock below threshold
low_stock_items = []
for item in inventory:
    if item["stock"] < threshold:
        low_stock_items.append(item)
#Output:
if len(low_stock_items) > 0:
    print("Low stock items found:")
    for item in low_stock_items:
        print(f"- {item['name']}: {item['stock']}")
else:
    print("No low stock items.")


##Create
#Query 1: Place a new order for an item and quantity.

#Input
item_id = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))

exists = False
in_stock = False
total_price = 0

new_order_id_number = 103
new_order_id = "Order_" + str(new_order_id_number)

#Process
for inventory_item in inventory:
    if inventory_item["item_id"] == item_id:
        exists = True
        if inventory_item["stock"] >= quantity:
            in_stock = True
            inventory_item["stock"] = inventory_item["stock"] - quantity
            total_price = inventory_item["unit_price"] * quantity
        break

if exists:
    if in_stock:
        Orders.append({
            "Order iD": new_order_id,
            "Item ID": item_id,
            "Quantity": quantity,
            "Status": "Placed",
            "Total": total_price
        })

#Output:
print(inventory)
print("-------------------")
print(Orders)
print("-------------------")
print("Item ID:", item_id)
print("Quantity ordered:", quantity)
print("New Stock:", inventory_item["stock"])


##Read
#Query 2: View all orders placed for a particular item — prompt the user to enter the item name

#Input:
search_item = input("Enter the item name to search (e.g. 'Latte'): ")

#Process: Match search item with item ID
item_exists = False
selected_item_id = None

for item_orders in inventory:
    if item_orders["name"] == search_item:
        item_exists = True
        selected_item_id = item_orders["item_id"]

#Output:
if item_exists == False:
    print("Item not found.")
else:
    matching_orders = []

    for order in Orders:
        if order["Item ID"] == selected_item_id:
            matching_orders.append(order)

    if matching_orders == []:
        print("No orders found for this item.")
    else:
        print("Matching orders:")
        for order in matching_orders:
            print(order)


#Query 3: Calculate and print the total number of orders placed for "Cold Brew".

#Input:
search_name = "Cold Brew"

#Process: Count number of placed orders for item
found_item_id = None

for item in inventory:
    if item["name"] == search_name:
        found_item_id = item["item_id"]

if found_item_id is None:         
    print("Not found")

if found_item_id is not None:
    order_count = 0

    for order in Orders:
        if order["Item ID"] == found_item_id:
            order_count = order_count + 1
#Output
    print("Total number of orders placed for Cold Brew:", order_count)


##Update
#Query 4: Prompt the user to enter an item id and new quantity. Update the item stock quantity

#Input:
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))

#Process: Update quantity
item_found = False

for item in inventory:
    if item["item_id"] == item_id:
        item["stock"] = new_stock
        item_found = True
        break

#Output:
if item_found == True:
    for item in inventory:
        if item["item_id"] == item_id:
            print(item["name"], "stock:", item["stock"])
else:
    print("Item not found.")

##Delete
#Query 5: Cancel an order and restore stock.

#Input:
cancel_order_id = input("Enter Order ID to cancel: ")

#Process: Cancel order
order_cancel = None

for order in Orders:
    if order["Order iD"] == cancel_order_id:
        order_cancel = order
        break

if order_cancel is None:
    print("Order not found")

else:
    if order_cancel["Status"] == "Cancelled":
        print("Order already cancelled")
    else:
        order_cancel["Status"] = "Cancelled"
        item_id = order_cancel["Item ID"]
        quantity = order_cancel["Quantity"]

        for item in inventory:
            if item["item_id"] == item_id:
                item["stock"] = item["stock"] + quantity
                updated_stock = item["stock"]
                break
            
#Output
        print("Cancelled Order:", order_cancel["Order iD"])
        print("Item ID:", item_id)
        print("Quantity:", quantity)
        print("Status:", order_cancel["Status"])
        print("Updated Stock:", updated_stock)
