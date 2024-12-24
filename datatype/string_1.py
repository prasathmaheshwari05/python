stat="good afternoon"
print(len(stat))
print(stat[1])
print(stat[3])
print(stat[5])
print(stat[6])
print(stat[-9::])
#different quotes and same sentence
timi='it "is 12pm'
print(timi)
#same quotes and same sentence
timi='it \'is 12pm'
print(timi)

#directly concatinate 
name="prasath"
age=21
# print(name,str(age))
print(f'{name}  {age}')

lis=["prasath","gobi",['abs',"arun"],"sundara"]
print(lis[2][0])