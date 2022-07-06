class Brick:
    _x = 0
    _y = 0
    _width = 0
    _height = 0
    _color = 0 #TODO: код цвета

    def __init__(self, x: int = 0, y: int = 0, width: int = 10, height: int = 10, color = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        # TODO: реализовать


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if val < 0:
            self._x = 0
        else:
            self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        if val < 0:
            self._y = 0
        else:
            self._y = val

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        if val <= 0:
            self._width = 10
        else:
            self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        if val <= 0:
            self._height = 10
        else:
            self._height = val

    @property
    def color(self):
        return self._color

    @color.setter
    def height(self, val):
        # TODO: сделать проверку ошибок
        self._color = val