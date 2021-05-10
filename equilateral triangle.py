print("Equilateral Triangle") 

def equitri_():    

    s = input("Side = ")    

    s = float(s)    

    A = ((3**(1/2))/4) * s*s    

    p = 3*s    

    print("Area = ",A,"sq units")    

    print("Perimeter = ",p,"units") 

while True:       

    equitri_()        

    if input() == "quit":           

        break