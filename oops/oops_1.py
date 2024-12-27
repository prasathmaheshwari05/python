class Bank_account:
    def __init__(self):
        self.name=''
        self.amount=0
        self.address=''
        self.accountno=0
    def creating(self):
        self.name=input("enter a name:")
        self.amount=int(input("enter amount"))
        self.address=input("enter your addres")
        self.accountno=int(input('enter account no'))
    def display(self):
        print('-'*50)
        print('your name is',self.name)
        print('your amount is',self.amount)
        print('your address is',self.address)
        print('your account no is',self.accountno)
def main():
    user=Bank_account()
    print('CREATING A ACOOUNT')
    user.creating()
    user.display()
    user2=Bank_account()
    print('CREATING second ACOOUNT')
    user2.creating()
    user2.display()
   

if __name__=='__main__':
    main()