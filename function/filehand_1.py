import os
def createfile(file_name):
    if (os.path.exists(file_name)):
        print('file already create')
    else:
        print('file now created')
        file=open(file_name,'w')




def main():
    print('enter a file you want')
    file_name=input()
    createfile(file_name)
if __name__=='__main__':
    main()