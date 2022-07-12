class Brick:
    _x = 0.
    _y = 0.
    _width = 1.
    _height = 1.
    _color = 'red'

    def __init__(self, x: float = 0., y: float = 0., width: float = 1., height: float = 1., color = 'red'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


    def collide_test_with_brick(self, second_brick):
        # Если хоть одна из точек второго прямоугольника попадает внутрь, то столкновение есть
        for point in second_brick.get_points():
            if self.is_point_inside(point[0], point[1]):
                return True
        else:
            return False

    # Нумерация точек идет от верхнего левого угла по часовой стрелке
    def get_points(self):
        return [[self._x, self._y],
                [self._x + self._width, self._y],
                [self._x + self._width, self._y + self._height],
                [self._x, self._y + self._height]]

    def is_point_inside(self, x: float, y: float):
        if self._x <= x <= (self._x + self._width) \
                and self._y <= y <= (self._y + self._height):
            return True
        else:
            return False

    def is_brick_out_of_scene(self, scene_width: float, scene_height: float):
        if self._x < 0.:
            return True
        elif self._x + self._width > scene_width:
            return True
        elif self._y < 0.:
            return True
        elif self._y + self._height > scene_height:
            return True
        else:
            return False

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
    def color(self, val):
        # TODO: сделать проверку ошибок
        self._color = val