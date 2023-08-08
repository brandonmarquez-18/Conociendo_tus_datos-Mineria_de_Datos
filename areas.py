import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

def calculate_square_area(side):
    area = side**2
    return area

def calculate_triangle_area(base, height):
    area = (base * height) / 2
    return area

def get_radius():
    radius = float(input("Enter the radius of the circle: "))
    return radius

def get_side():
    side = float(input("Enter the side length of the square: "))
    return side

def get_base_height():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return base, height

def main():
    option = input("Select a geometric shape to calculate its area (circle, square, triangle): ")

    if option == "circle":
        radius = get_radius()
        area = calculate_circle_area(radius)
        print("The area of the circle is:", area)
    elif option == "square":
        side = get_side()
        area = calculate_square_area(side)
        print("The area of the square is:", area)
    elif option == "triangle":
        base, height = get_base_height()
        area = calculate_triangle_area(base, height)
        print("The area of the triangle is:", area)
    else:
        print("Invalid option. Please select a valid geometric shape.")

if __name__ == "__main__":
    main()
