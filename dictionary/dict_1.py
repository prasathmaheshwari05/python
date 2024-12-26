# watch={"titon":4567,"fasttrack":2345,"sonata":4545,"fasttrack":9000,"model":4545}
# print("watch",len(watch))
# print(watch["titon"])
# print(watch["fasttrack"])
# print(watch)
# #modify,it is mutable datatype
# watch["titon"]=20000
# print(watch)
# #type
# print(type(watch))
# print('-'*50)



#dict methodd
emp={"empname":'prasath',"jobid":4568,"is_active":True,'package':7.5}
print('get method',emp.get("empname"))
print('key method',emp.keys())
print('values method',emp.values())
print('items method',emp.items())
#it remove last value
pop=emp.popitem()
print("popitme method",pop)
print(emp)
#pop using dict ,it given key value
pops=emp.pop('empname')
print("pop method",pop)
print(emp)

#update method
emp.update({5.0:"packages"})
print("update",emp)
