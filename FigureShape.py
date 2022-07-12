from Brick import Brick

class FigureShape:
    __pose_count: int = 0 # количество вращательных позиций, доступных фигуре
    __cur_pose: int = 0 # текущая вращательная позиция
    __poses: map = None # набор всех вращательных позиций фигуры

    def __init__(self, shape_type: int, brick_width: float, brick_height: float):
        #TODO: реализовать
        if shape_type == 0: # т-shape
            self.bricks = [Brick(0., 0.), Brick(brick_width, 0.), Brick(2.*brick_width, 0.), \
                            Brick(brick_width, brick_height)]

        elif shape_type == 1: # square shape
            self.bricks = [Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(0., brick_height), Brick(brick_width, brick_height)]

        elif shape_type == 2: # z-shape
            self.bricks = [Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(0. + brick_width, brick_height), Brick(2.*brick_width, brick_height)]

        elif shape_type == 3: # s-shape
            self.bricks = [Brick(brick_width, 0.), Brick(2.*brick_width, 0.), \
                           Brick(0., brick_height), Brick(brick_width, brick_height)]

        elif shape_type == 4: # Г - shape
            self.bricks = [Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(0., brick_height), Brick(0., 2.*brick_height), Brick(0., 3.*brick_height)]

        elif shape_type == 5: # mirrored Г-shape
            self.bricks = [Brick(0., 0.), Brick(brick_width, 0.), \
                           Brick(brick_width, brick_height), Brick(brick_width, 2. * brick_height), Brick(brick_width, 3. * brick_height)]

        elif shape_type == 6:  # |-shape
            self.bricks = [Brick(0., 0.), Brick(0., brick_height), \
                            Brick(0., 2.*brick_height), Brick(0., 3.*brick_height), Brick(0., 4.*brick_height)]

        else:
            #TODO: написать свой класс исключений. Кинуть исключение FigureShapeError
            raise ValueError

        # Устанавливаем координаты фигуры

        # Устанавливаем поворот фигуры


    def get_bricks(self):
        return

    def move_hor_on(self, x_delta: float):
        return

    def move_vert_on(self, y_delta: float):
        return

    def set_xy(self, x: float, y: float):
        return

