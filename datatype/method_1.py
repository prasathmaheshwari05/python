#append
list_1=["apple","graps"]
list_1.append("watermelon")
print(list_1)
#insert
list_1.insert(0,"icecream")
print(list_1)

#extend
list_1.extend(["gova","pomogranate"])
print(list_1)
list_1.extend("gova")#stringgggggggggg
print(list_1)
# list_1.extend(True)
# print(list_1)

#removing method
list_1.pop(0)
print(list_1)
list_1.remove("apple")
print(list_1)
#first on;y it take
city=["chennai","pune","bangalue","chennai"]
city.remove("chennai")
print(city)

state=['tamilnadu',"bagalur",'pune',"pune"]
print(state.index("tamilnadu"))
print(state.count("pune"))