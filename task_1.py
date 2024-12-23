food=["burger","veg pizza","momos","Chinese","garlic bread","french fries","non-veg","pizza"]
print("Food available at restaurant",food,type(food))
food.pop(0)
print("total food in item :",len(food))
food.append("kabab")
print(food)
del food[2:5]
# print(food)
foodnot=["momos","Chinese","garlic bread"]
print("food is present not available",foodnot)