print("Kite")
def kite():
    d = float(input("Diagnol 1 = "))
    D = float(input("Diagnol 2 = "))
    a = float(input("Side 1 = "))
    b = float(input("Side 2 = "))
    A = (d*D)*(1/2)
    p = 2*(a+b)
    print("Area = ",A,"sq units");print("Perimeter = ",p,"units")
while True:
    kite()
    if input() == "quit":
        break    