print("Welcome to Pentagon.py")
def Regular_Pentagon():
    Side = float(input("Side = "))
    Area = (1/4)*((5*(5+2*(5**(1/2))))**(1/2)) * (Side * Side)
    Perimeter = 5*Side
    Diagonal = ((1+(5**(1/2)))/2)* Side
    print("Area = ", Area, "sq units")
    print("Perimeter = ", Perimeter, "units");print("Diagonal = ", Diagonal, "units")
    
while True:
    Regular_Pentagon()
    if input() == "quit()":
        break    