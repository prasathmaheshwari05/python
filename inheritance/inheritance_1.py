#parent class
class person:
    def __init__(self,idcard,Name):
        self.id=idcard
        self.name=Name
    def displayinfo(self):
        print(f'id is{self.id} name: {self.name}')
    
#child clsass
class employee(person):
    def show(self):
        print('show')



# ob1=person(101,'prasath')
ob1=employee(101,'prasath')
ob1.displayinfo()
ob1.show()