inventory = []
    {"product_id": 1, "stock": 10}, 
    {"product_id": 1, "stock": 10}, 
    {"product_id": 1, "stock": 10}, 
    {"product_id": 1, "stock": 10}, 
}

# Are ALL items in stock?
all_in_stock = all(qty > 0 for qty in inventory.values())

print(f"All in stock? : {all_in_stock}") # Output: All in stock? : False ❌

# Is ANY item out of stock?
any_sold_out = any(qty == 0 for qty in inventory.values())

print(f"Any item out of stock? : {any_sold_out}") # Output: Any item out of stock? : True ✅

print(sorted(inventory,lambda:x:inventory[])
