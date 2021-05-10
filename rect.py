print("Rectangle")
def rect():
    l = float(input("Lenght = "))
    b = float(input("Breadth = "))
    A = l*b
    p = 2*(l+b)
    d = ((l*l)+(b*b))**(1/2)
    print("Area = ",A,"sq units")
    print("Perimeter = ",p,"units")
    print("Diagnol = ",d,"units")
while True:
    rect()
    if input() == "quit":
        break    