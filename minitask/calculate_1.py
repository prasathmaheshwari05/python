def add(num1,num2):
    return (num1+num2)
def sub(num1,num2):
    return (num1-num2)
def multi(num1,num2):
    return (num1*num2)
def divi(num1,num2):
    return (num1/num2)
def floordiv(num1,num2):
    return (num1//num2)
def expo(num1,num2):
    return (num1**num2)



def main(op):
    if op=='+':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        adds=add(num1,num2)
        print(adds)
    elif op=='-':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        subs=sub(num1,num2)
        print(subs)
    elif op=='*':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        mul=multi(num1,num2)
        print(mul)
    elif op=='/':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        div=divi(num1,num2)
        print(div)
    elif op=='//':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        fd=floordiv(num1,num2)
        print(fd)
    elif op=='**':
        num1=int(input("enter a first number:"))
        num2=int(input("enter a second number"))
        ex=expo(num1,num2)
        print(ex)


if __name__=='__main__':
    op=input("enter a symbol:")
    main(op)