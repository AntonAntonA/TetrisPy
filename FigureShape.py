from Brick import Brick

class FigureShape:
    __pose_count: int = 0 # количество вращательных позиций, доступных фигуре
    __cur_pose: int = 0 # текущая вращательная позиция
    __poses: list = None # набор всех вращательных позиций фигуры. Фигуры вращаются по часовой стрелке
    __speed: list = None # Вектор скорости фигуры

    def __init__(self, shape_type: int, x: float, y: float, brick_width: float, brick_height: float, rotate_count: int,
                 speed: list):
        #TODO: реализовать
        if shape_type == 0: # т-shape
            self.__poses = [[Brick(0., 0.), Brick(brick_width, 0.), Brick(2.*brick_width, 0.),
                                Brick(brick_width, brick_height)],
                            [Brick(0., 0.), Brick(brick_width, 0.), Brick(brick_width, -brick_height),
                                Brick(brick_width, brick_height)],
                            [Brick(0., 0.), Brick(brick_width, 0.), Brick(2.*brick_width, 0.),
                                Brick(brick_width, -brick_height)],
                            [Brick(brick_width, 0.), Brick(brick_width, -brick_height), Brick(brick_width, brick_height),
                                Brick(2*brick_width, 0.)]
                            ]

        elif shape_type == 1: # square shape
            self.__poses = [[Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(0., brick_height), Brick(brick_width, brick_height)]]

        elif shape_type == 2: # z-shape
            self.__poses = [[Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(0. + brick_width, brick_height), Brick(2.*brick_width, brick_height)]]

        elif shape_type == 3: # s-shape
            self.__poses = [[Brick(brick_width, 0.), Brick(2.*brick_width, 0.), \
                           Brick(0., brick_height), Brick(brick_width, brick_height)]]

        elif shape_type == 4: # Г - shape
            self.__poses = [[Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(0., brick_height), Brick(0., 2.*brick_height), ]]

        elif shape_type == 5: # mirrored Г-shape
            self.__poses = [[Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(brick_width, brick_height), Brick(brick_width, 2. * brick_height)]]

        elif shape_type == 6:  # |-shape
            self.__poses = [[Brick(0., 0.), Brick(0., brick_height), \
                            Brick(0., 2.*brick_height), Brick(0., 3.*brick_height)]]

        else:
            #TODO: написать свой класс исключений. Кинуть исключение FigureShapeError
            raise ValueError

        self.__pose_count = len(self.__poses)

        # Устанавливаем координаты фигуры
        self.set_xy(x, y)

        # Устанавливаем поворот фигуры
        i = 0
        while i < rotate_count:
            self.rotate_right()
            i += 1

        # Устанавливаем скорость фигуры
        self.__speed = speed

    def get_bricks(self):
        return self.__poses[self.__cur_pose]

    def move_hor_on(self, x_delta: float):
        for figure_pose in self.__poses:
            for brick in figure_pose:
                brick.x = brick.x + x_delta
        return

    def move_vert_on(self, y_delta: float):
        for figure_pose in self.__poses:
            for brick in figure_pose:
                brick.y = brick.y + y_delta
        return


    def get_speed(self):
        return self.__speed

    def set_x_speed(self, val):
        self.__speed[0] = val

    def set_y_speed(self, val):
        self.__speed[1] = val


    def get_pivot_xy(self):
        return self.__poses[0][0].get_points()[0]

    def set_xy(self, x: float, y: float):
        cur_xy = self.get_pivot_xy()
        x_delta = x - cur_xy[0]
        y_delta = y - cur_xy[1]
        self.move_hor_on(x_delta)
        self.move_vert_on(y_delta)
        return

    def rotate_left(self):
        self.__cur_pose -= 1
        if self.__cur_pose < 0:
            self.__cur_pose = self.__pose_count - 1
        return

    def rotate_right(self):
        self.__cur_pose += 1
        if self.__cur_pose >= self.__pose_count:
            self.__cur_pose = 0
        return

