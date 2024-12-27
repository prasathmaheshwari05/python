import arithmatic 
print('enter 1/2/3 option')
select=int(input())
def main():
    num1=int(input("enter one num"))
    num2=int(input("enter second num"))
    if(select==1):
        ans=arithmatic.addition(num1,num2)
        print('addition',ans)
    elif(select==2):
        sub=arithmatic.subtraction(num1,num2)
        print('subtraction operation:',sub)
    elif(select==3):
        mul=arithmatic.multiplication(num1,num2)
        print('multiplication operation:',mul)
    else:
        
        print('plese select only three number')
if __name__=='__main__':
    main()