print("Wellcome to PARALLELOGRAM.py")
def parallelogram():
    side = float(input("Side = "))
    base = float(input("Base = "))
    height = float(input("Height = "))
    area = base*height
    perimeter = 2*(side + base)
    print("Area = ", area, "sq units")
    print("Perimeter = ", perimeter, "units")

while True:
    parallelogram()
    if input() == "exit":
        break    