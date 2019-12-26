from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

def main():
    rectangle = Rectangle(3, 2, "blue")
    circle = Circle(5, "green")
    square = Square(5, "red")
    print(rectangle)
    print(circle)
    print(square)

if __name__ == "__main__":
    main()