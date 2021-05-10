print("Isosceles Triangle")
def isctri():
    a = input("Common side : ")
    b = input("Base : ")
    a = float(a)
    b = float(b)
    A = (b/2)*(((b*b)-(a*a))**(1/2))
    p = (2*a)+b
    h = 2*(A/b)
    print("Area = ", A,"sq units")
    print("Perimeter = " , p,"units")
    print("Height = ", h,"units")
while True:
    isctri()
    if input() == "exit":
        break    