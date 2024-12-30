#parent class
class person:
    def __init__(self,idcard,Name):
        self.id=idcard
        self.name=Name
    def displayinfo(self):
        print(f'id is{self.id} name: {self.name}')
    
#child clsass
class employee(person):
    def __init__(self,idcard,Name,salaray):
        super().__init__(idcard,Name)
        self.sal=salaray


ob1=person(101,'prasath')
ob1.displayinfo()
ob2=employee(101,'prasath',2500000)
ob2.displayinfo()
print(ob2.sal)