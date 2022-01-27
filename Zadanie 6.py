import math

print("1. Calculate a surface area of a rectangle")
print("2. Calculate a surface area of a square")
print("3. Calculate a surface area of a triangle")
print("4. Calculate a surface area of a trapezium")
print("5. Calculate a surface area of a circle")

while True:

    figure_choice = input("Tell me, which figure you have chosen: ")

    def rectangle(value_a,value_b):
        return value_a * value_b

    def square(value_a):
        return value_a * value_a

    def triangle(value_a,value_b):
        surface_area = value_a * value_b / 2
        print("Triangle surface area is: ", surface_area)

    def trapezium(value_a, value_b, value_c):
        surface_area = (value_a + value_b) / 2 * value_c
        print("Trapezium surface area is: ", surface_area)

    def circle(value_a):
        surface_area = math.pi * value_a ** 2
        print("Circle surface area is: ", surface_area)

    if (figure_choice == "1"):
        value_a = int(input("Please, write parameter a: "))
        value_b = int(input("Please, write parameter b: "))
        rectangle(value_a, value_b)
        print("Rectangle surface area is: ", rectangle(value_a, value_b))

    elif (figure_choice == "2"):
        value_a = int(input("Please, write parameter a: "))
        square(value_a)
        print("Square surface area is: ", square(value_a))

    elif (figure_choice == "3"):
        value_a = int(input("Please, write parameter a: "))
        value_b = int(input("Please, write parameter b: "))
        triangle(value_a, value_b)

    elif (figure_choice == "4"):
        value_a = int(input("Please, write parameter a: "))
        value_b = int(input("Please, write parameter b: "))
        value_c = int(input("Please, write parameter c: "))
        trapezium(value_a, value_b, value_c)

    elif (figure_choice == "5"):
        value_a = int(input("Please, write parameter a: "))
        circle(value_a)

    elif (figure_choice == "0"):
        print("Thank you")
        break

    else:
        print("You have chosen wrong number, please try again")


"""
    
    import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h
"""