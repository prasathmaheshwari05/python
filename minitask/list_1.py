class list_:
   
    def __init__(self):
        self.li=[]
    def creating(self):
        self.list_1=eval(input('enter a list:'))
    def dis(self):
        print('this is list',self.list_1)
        if (self.list_1[0]<self.list_1[1])and(self.list_1[0]<self.list_1[2]):
            print('mimum',self.list_1[0])
        elif (self.list_1[1]<self.list_1[2]):
            print('mimum',self.list_1[1])
        else:
            print('mimum',self.list_1[2])
        if (self.list_1[0]>self.list_1[1])and(self.list_1[0]>self.list_1[2]):
            print('maximum',self.list_1[0])
        elif (self.list_1[1]>self.list_1[2]):
            print('maximum',self.list_1[1])
        else:
            print('maximum',self.list_1[2])
        total=0
        for i in self.list_1:
            total=total+i
        print('total',total)
def main():
    user=list_()
    user.creating()
    user.dis()
if __name__=='__main__':
    main()
