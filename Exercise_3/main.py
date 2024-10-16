shopping_list = {}
item_limit = 3

for item_count in range(item_limit):
    print(f"Enter item {item_count + 1}: ")
    item = input()
    
    print(f"Enter quantity for {item}: ")
    quantity = int(input())
    
    shopping_list[ item ] = quantity

print("Your shopping list: ")
for item, quantity in shopping_list.items():
    print(f"- {quantity} {item}")

