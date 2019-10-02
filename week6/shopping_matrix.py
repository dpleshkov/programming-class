#Bought groceries at 2 different stores
groceries = [
    [["Safeway", "Cheese", 4], ["Safeway", "Eggs", 3], ["Safeway", "Milk", 4], ["Safeway", "Bread", 5]], 
    [["Whole Foods", "Cheese", 9], ["Whole Foods", "Eggs", 8], ["Whole Foods", "Milk", 10], ["Whole Foods", "Bread", 13]]
]

#Calculates cost per shop
safeway = 0
whole_foods = 0

for item in groceries[0]:
    safeway += item[2]

for item in groceries[1]:
    whole_foods += item[2]

print("Total Safeway Cost: ${}".format(safeway))
print("Total Whole Foods Cost: ${}\n".format(whole_foods))


#Calculates cost per ingredient
ingredient_costs = {
    "Cheese": 0,
    "Eggs": 0,
    "Milk": 0,
    "Bread": 0
}

for item in groceries[0]:
    ingredient_costs[item[1]] += item[2]

for item in groceries[1]:
    ingredient_costs[item[1]] += item[2]

for item in ingredient_costs:
    print("Total {} cost across stores: ${}".format(item, ingredient_costs[item]))

