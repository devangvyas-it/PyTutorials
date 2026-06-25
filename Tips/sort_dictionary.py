inventory = [
    {"product_id": 1, "stock": 10}, 
    {"product_id": 2, "stock": 15}, 
    {"product_id": 3, "stock": 5}, 
    {"product_id": 4, "stock": 0}, 
]

print(sorted(inventory, key=lambda x: x["stock"], reverse=False))