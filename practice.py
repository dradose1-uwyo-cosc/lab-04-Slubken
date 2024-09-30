items = ["Steak" "Milk" "Eggs" "water" "Tea"]
prices = [10, 5, 2, 4, 2]

for i in range(len(items)):
    print (f"I bought {items[i]} for ${prices[i]}")
total = 0

for t in prices:
    total = total + t
print(f"I spent ${total} at Walmart")