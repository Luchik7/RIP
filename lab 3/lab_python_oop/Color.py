class Color:
    def __init__(self):
        self.__color = None

    @property
    def color_prop(self):
        return self.__color

    @color_prop.setter
    def color_prop(self, value):
        self.__color = value