# Fantasy game inventory

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for item,number in inventory.items():
        item_total += number
        print(f"{number} {item}")
    print(f"Total number of items: {item_total}")

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

display_inventory(stuff)

# List to dictionary

def add_to_inventory(inventory, items):
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item]+=1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)


