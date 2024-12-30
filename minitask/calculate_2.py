class dic:
    def __init__(self):
        self.num1=0
        self.num2=0
    def create(self):
        self.num1=int(input('enter a first number'))
        self.num2=int(input('enter a second number'))
    def display(self):
        print('first number',self.num1)
        print('second number',self.num2)
    def add(self):
        return (self.num1+self.num2)
    def sub(self):
        return (self.num1-self.num2)
    def multi(self):
        return (self.num1*self.num2)
    def divi(self):
        return (self.num1/self.num2)
    def floordiv(self):
        return (self.num1//self.num2)
    def expo(self):
        return (self.num1**self.num2)

def main(op):
    user=dic()
    user.create()
    user.display()
    if op=='+':
        adds=user.add()
        print(adds)
    elif op=='-':
        
        subs=user.sub()
        print(subs)
    elif op=='*':
        
        mul=user.multi()
        print(mul)
    elif op=='/':
        
        div=user.divi()
        print(div)
    elif op=='//':
        
        fd=user.floordiv()
        print(fd)
    elif op=='**':
        
        ex=user.expo()
        print(ex)


if __name__=='__main__':
    op=input("enter a symbol:")
    main(op)