class food:
    def __init__(self):
        self.food=[]
    def creating(self):
        self.food=eval(input('enter a list'))
    def display(self):
        print('this is list')
    def displays(self):
        print(self.food)
    def add(self):
        self.food.append('idli')
        print(self.food)
    def update(self):
        self.food[1]='hydrabad briyani'
        print(self.food)
    def delete(self):
        self.food.remove('parotta')
        print(self.food)
def main(op):
    user=food()
    user.creating()
    user.display()
    if op==1:
        user.displays()
    elif op==2:
        user.add()
    elif op==3:
        user.update()
    elif op==4:
        user.delete()

if __name__=='__main__':
    op=int(input("enter a number:"))
    main(op)
