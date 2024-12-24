roll_number=(123,124,125,126,127,123)
mix_type=("prasath",123,True,78.9)
#type
print(type(roll_number))
print(type(mix_type))
#len
print(len(roll_number))
print(len(mix_type))
#positive
print("using positive index",mix_type[0])
print("using positive index",mix_type[2])
mix=mix_type[-3:-1]
print("using negative index",mix)
rol=roll_number[-4:-1]
print("using negative index",rol)

#single tuple create 
roll=123
print(type(roll))
rolls=(123,)
print(type(rolls))