import os
def readfile(filename):
    if(os.path.exists(filename)):
        fd=open(filename,'r')
        data=fd.read()
        createfile(data)
        fd.close()
def createfile(data):
    fds=open('demo.txt','w')
    fds.write(data)
    print('content add succesfully')
    fds.close


def main():
    print('enter the file')
    filename=input()
    readfile(filename)
if __name__=="__main__":
    main()