def fullname(firstname,lastname,national='indian'):
    return f'name is {firstname} {lastname} your nationality {national}'
def main():
    result=fullname('prasath','sundararajan')
    print("position arugument:",result)
    result=fullname('prasath','sundararajan','maheswari')
    print("position arugument:",result)
    result=fullname(lastname='prasath',firstname='sundararajan')
    print("keyward arugument:",result)
    result=fullname('prasath','sundararajan',national='other')
    print("keyword arugument:",result)

if __name__=="__main__":
    main()


def circle(pi,r):
    return ((pi)*(r*r))
def main():
    result=circle(3.14,5)
    print("radius of circle",result)
    #keyword argument
    result=circle(pi=3.14,r=5)
    print("radius of circle",result)
    result=circle(3.14,5)
    print("radius of circle",result)
    result=circle(3.14,5)
    print("radius of circle",result)

if __name__=="__main__":
    main()

#default arugument
def circle(r,pi=3.14):
    return ((pi)*(r*r))
def main():
    result=circle(5)
    print("radius of circle",result)
if __name__=="__main__":
    main()