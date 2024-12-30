list_1=eval(input('enter a number:'))
# print(list_1[0])
if (list_1[0]<list_1[1])and(list_1[0]<list_1[2]):
    print('mimum',list_1[0])
elif (list_1[1]<list_1[2]):
    print('mimum',list_1[1])
else:
    print('mimum',list_1[2])
if (list_1[0]>list_1[1])and(list_1[0]>list_1[2]):
    print('maximum',list_1[0])
elif (list_1[1]>list_1[2]):
    print('maximum',list_1[1])
else:
    print('maximum',list_1[2])
total=0
for i in list_1:
    total=total+i
print('total',total)


# list_1=eval(input('enter a number:'))
# max=list_1[0]
# min=list_1[0]
# tot=0
# for i in list_1:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
#     tot=tot+i
    
# print(max)
# print(min)
# print(tot)
