class circle:
    pi=3.14 #class varaiable
    def __init__(self):
        self.radius=0
    def accept(self):
        self.radius=int(input('enter your radius:'))
    def dis(self):
        print('area of circle',(circle.pi*(self.radius*self.radius)))
def main():
    cir=circle()
    cir.accept()
    cir.dis()
if __name__=='__main__':
    main()