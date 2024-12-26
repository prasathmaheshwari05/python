def demo_1():
    print("inside demo")
def demo_2(value1,value2):
    print("inside demo",value1,value2)
    print("addition",value1+value2)
def demo_3(value1,value2):
    print("inside demo",value1,value2)
    add=value1+value2
    sub=value1-value2
    return add,sub

def main():
    demo_1()
    demo_2(12,5)
    tot=demo_3(100,150) 
    print("additio",tot[0])
    print("sub",tot[1])



if __name__=='__main__':
    main()



