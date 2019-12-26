from lab_python_oop.Rectangle import Rectangle

class Square(Rectangle):

    FIGURE_TYPE = "Square"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, side_size, color):
        self.side = side_size
        super().__init__(self.side, self.side, color)

    def __repr__(self):
        return "{} color: {}, side: {}, area: {}".format(
            Square.get_figure_type(),
            self.color.color_prop,
            self.side,
            self.area()
        )