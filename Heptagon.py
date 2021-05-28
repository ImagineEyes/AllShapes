print("Heptagon")


def regular_heptagon():
    side = float(input("Side = "))
    area = (7 / 4) * (side * side) * 2.0765   # 3.634 * side*side
    perimeter = 7 * side
    print("Area = ", area, "sq units")
    print("Perimeter = ", perimeter, "units")


while True:
    regular_heptagon()
    if input() == "quit":
        break
