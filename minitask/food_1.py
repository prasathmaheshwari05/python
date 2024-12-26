
food=['chicken rice','biriyani','parotta']
def display():
    print(food)
def add():
    food.append('idli')
    print(food)
def update():
    food[1]='hydrabad briyani'
    print(food)
def delete():
    food.remove('parotta')
    print(food)



def main(op):
    if op==1:
        display()
    elif op==2:
        add()
    elif op==3:
        update()
    elif op==4:
        delete()


if __name__=='__main__':
    op=int(input("enter a number:"))
    main(op)