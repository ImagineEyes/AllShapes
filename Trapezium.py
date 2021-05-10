print("Welcome to 'Tapezium.py'")
def Trapezium():
    Base = float(input("Base(One of the parellel side) = "))
    Opp_Base = float(input("Side opposite to the Base = "))
    Height = float(input("Height = "))
    Side1 = float(input("One of the side = "))
    Side2 = float(input("Another side = "))
    Area = (1/2)*(Base + Opp_Base) * Height
    Perimeter = Base + Opp_Base + Side1 + Side2
    print("Area = ", Area,"sq units");print("Perimeter = ", Perimeter,"units")

while True:
    Trapezium()
    if input() == "quit()":
        break
