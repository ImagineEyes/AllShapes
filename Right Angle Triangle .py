print("Right Angled Triangle")
def RAT_():
    h = input("Height = ")
    b = input("Base = ")
    h = float(h)
    b = float(b)
    H = ((h*h)+(b*b))**(1/2)
    a = (h*b)/2
    p = h+b+H
    print("Area = ",a,"sq units")
    print("Perimeter = ",p,"units")
    print("Hypotenuse = ",H,"units")
while True:
    RAT_()
    if input() == "exit" or "quit":
        break