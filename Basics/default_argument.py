def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))

def add_item_updated(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item_updated("A"))
print(add_item_updated("B"))
