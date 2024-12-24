emp=("prasath",234,"traing")
(name,id,role)=emp
print(name)



emp=("prasath",234,"traing","admin","developer")
(name,*id,role)=emp
print(name)
print(role)
print(id)