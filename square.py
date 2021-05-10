print("Square")
def square():
    s = float(input("Side = "))
    A = s*s
    p = 4*s
    d = ((2)**(1/2))*s
    print("Area = ", A, "sq units")
    print("Perimeter = ", p, "units")
    print("Diagonal = ", d, "units")
while True:
    square()
    if input() == "exit":
        break