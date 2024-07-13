
# Practical Task 2

menu = ['bread', 'fish', 'coffee', 'rabbits']
stock = {'bread': 20, 'fish': 30, 'coffee': 40, 'rabbits': 7}
price = {'bread': 1.50, 'fish': 2.50, 'coffee': 3.75, 'rabbits': 0.12}


# calc

total_stock = 0
for item in menu:
    item_cost = stock[item] * price[item]
    print(f"Cost of item {item}: £{float('{:.2f}'.format(item_cost))}")