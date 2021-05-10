print("Quadrilateral")
def quad():
    a = float(input("Longest diagnol = "))
    b = float(input("One of the small diagnol = "))
    c = float(input("Another small diagnol = "))
    A = ((1/2*a*b)+(1/2*a*c))
    print("Area = ",A,"sq units")
    print("Perimeter = Sum of all sides ")
while True:
    quad()
    if input() == "exit":
        break    