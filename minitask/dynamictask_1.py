# #dynamic list which contain 5 element in float
output=[]
tot=int(input("enter tot number:"))
print("enter a value")
for i in range(tot):
    value=float(input())
    output.append(value)
print(output)
print("-"*50)


#dynamic list which contain 5 element in string
output=[]
tot=int(input("enter tot number:"))
print("enter a value")
for i in range(tot):
    value=input()
    output.append(value)
print(output)
print("-"*50)

fruit=['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]
print(fruit[0])
print(fruit[1])
print(fruit[1][0])
print(fruit[1][1])
print(fruit[3][0])
print(fruit[3][1])
print("-"*50)


#iterate for loop range function
Menu=['dal','paneer','kofta','tawa panner','rice','roti']
for i in range(len(Menu)):
    print(Menu[i])

# #iterate for loop range function
author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')
for i in range(len(author_name)):
    print(author_name[i])

# #timing
timing='it\ \'s 7.30am'
print(timing)
print("-"*50)

# #input
name=input()
sal=int(input())
company=input()
print("enter employee name :",name)
print("enter salary :",sal)
print("Company :",company)
print("-"*50)

#printing employee details
emp=[{"name":"prasath","sal":"1500000","company":"changepond"}]
print("name","sal","company")
for i in emp:
    print(i["name"],i["sal"],i["company"])
print("-"*50)

# #string
print("print('hello world')")
print("'E\changepondNewBatch\python'")

#iterate while loop
Menu=['dal','paneer','kofta','tawa panner','rice','roti']
i=0
while(len(Menu)>i):
    print(Menu[i])
    i=i+1

# #iterate while loop
author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')
i=0
while(len(author_name)>i):
    print(author_name[i])
    i=i+1
print("-"*50)

#for loop
for i in range(3,16,3):
    print(i)
print("-"*50)

i=3
while i<=range(16):
    print(i)
    i=i+3


for i in range(12,1,-3):
    print(i)


#list method
Menu=['dal','paneer','kofta','tawa panner','rice','roti']
Menu[3]='Malai Paneer'
print(Menu)
Menu[4:]='Tandoori roti','naan'
print(Menu)

#
i=123
add=0
while(i!=0):
    ld=i%10
    add=add+ld
    i=i//10
print(add)


