mix={"prasath",True,9.0}
mix.add("sundararajan")
print("add method",mix)
# mix.discard(True)
# print('discard method',mix)
# mix.remove(True)
# print('remove method',mix)
mix.pop()
print('pop method',mix)
print('-'*50)



#intersect method
company_1={'tcs','changepond','infous','cts'}
company_2={'tcs','fidas','cts','zoho'}
inter=company_1.intersection(company_2)
print("intersect op",inter)

#intersect method using & operator
company_1={'tcs','changepond','infous','cts'}
company_2={'tcs','fidas','cts','zoho'}
inter=company_1 & company_2
print("intersect op",inter)


#union method
company_1={'tcs','changepond','infous','cts'}
company_2={'tcs','fidas','cts','zoho'}
uni=company_1.union(company_2)
print("intersect op",uni)
#union using | operator
company_1={'tcs','changepond','infous','cts'}
company_2={'tcs','fidas','cts','zoho'}
uni=company_1 | company_2
print("intersect op",uni)

#update
company_1={'tcs','changepond','infous','cts'}
update_company={'tata','neon','tcs'}
company_1.update(update_company)
print("update comapny",company_1)

#difference
company_1={'tcs','changepond','infous','cts'}
company_2={'tcs','fidas','cts','zoho'}
dif=company_1.difference(company_2)
print("difference",dif)
