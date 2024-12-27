from sys import *
def addition(num1,num2):
    res=num1+num2
    return res
def main():
    print('application namr',argv[0])
    print('first argument name',argv[1])
    # print('second argumeny',argv[2])
    if(len(argv)==2):
        if(argv[1]=='--U'):
            print('pass argument pass first arugument and second argument')
            exit()
        if(argv[1]=='--H'):
            print('help application use to add two nmber')
            exit()
    if(len(argv)!=3):
        print('invalid input')
        print('please select --U')
        print('please select --H')
        exit()
    tot=addition(int(argv[1]),int(argv[2]))
    print('addition',tot)
if __name__=='__main__':
    main()