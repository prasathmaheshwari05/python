def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def multi(num1,num2):
    print(num1*num2)
def divi(num1,num2):
    print(num1/num2)
def floordiv(num1,num2):
    print(num1//num2)
def expo(num1,num2):
    print(num1**num2)



def main(op):
    if op=='+':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        add(num1,num2)
    elif op=='-':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        sub(num1,num2)
    elif op=='*':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        multi(num1,num2)
    elif op=='/':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        divi(num1,num2)
    elif op=='//':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        floordiv(num1,num2)
    elif op=='**':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        expo(num1,num2)


if __name__=='__main__':
    op=input("enter a symbol:")
    main(op)