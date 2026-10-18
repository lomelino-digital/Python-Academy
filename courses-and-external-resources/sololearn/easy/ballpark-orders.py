order = input()
price = 0
for i in range(4):
    if "Nachos" in order:
        price += 6
        order = order.replace("Nachos", "", 1)
    elif "Pizza" in order:
        price += 6
        order = order.replace("Pizza", "", 1)
    elif "Cheeseburger" in order:
        price += 10
        order = order.replace("Cheeseburger", "", 1)
    elif "Water" in order:
        price += 4
        order = order.replace("Water", "", 1)
    else:
        price += 5

print(price*1.07)
