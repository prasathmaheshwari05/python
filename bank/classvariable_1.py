class Bank_account:
    BankName='ICIC' #class variable
    ROI=5
    def __init__(self): #instance variable
        self.name=''
        self.amount=0
        self.address=''
        self.accountno=0
    def creating(self):#instance method
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
    @classmethod
    def disbankinfo(cls):
        print('display bank deatil')
        print("Bank Name",cls.BankName)
        print("Rate of Interest",cls.ROI)
    @staticmethod
    def displayKYCinfo():
        print('print your details')
        print('aadtha card',Bank_account.BankName)
        print('pan card')
        print('photo')
def main():
    # print("Bank Name",Bank_account.BankName)
    # print("Rate of Interest",Bank_account.ROI)
    Bank_account.disbankinfo()
    Bank_account.displayKYCinfo()
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
