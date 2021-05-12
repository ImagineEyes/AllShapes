print("Welcome to Hexagon.py")
def Regular_Hexagon():
    Side = float(input("Side = "))
    Area = ((3*(3**(1/2)))/2)*Side
    Perimeter = 6*Side
    print("Area = ", Area, "sq units");print("Perimeter = ", Perimeter, "units")
    
while True:
    Regular_Hexagon()
    if input() == "quit()":
        break