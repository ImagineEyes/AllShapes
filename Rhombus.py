print("Rhombus")
def rhombus():
    d = float(input("Diagonal 1 = "))
    D = float(input("Diagonal 2 = "))
    e = (1/2)*d
    f = (1/2)*D
    s = ((e*e)+(f*f))**(1/2)
    p = 2*((d*d)+(D*D))**(1/2)
    a = (1/2)*(d*D)
    print("Area = ",a,"sq units");print("Perimeter = ",p,"units");print("Side = ",s,"units")

while True:
    rhombus()
    if input() == "quit":
        break