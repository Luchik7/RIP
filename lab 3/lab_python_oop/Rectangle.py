from lab_python_oop.Color import Color
from lab_python_oop.figure import Figure

class Rectangle(Figure):

    FIGURE_TYPE = "Rectangle"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color()
        self.color.color_prop = color

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} color: {}, width: {}, height: {}, area: {}".format(
            Rectangle.get_figure_type(),
            self.color.color_prop,
            self.width,
            self.height,
            self.area()
        )