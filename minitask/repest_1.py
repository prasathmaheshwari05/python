list_1=eval(input("enter a list:"))
one=list_1
store=[]
store2=[]
for i in one:
    if i  not in store :
        store=[i]+store
    
    else:
        store2=[i]+store2
        print('this is repeated',i)
print(store)
      
