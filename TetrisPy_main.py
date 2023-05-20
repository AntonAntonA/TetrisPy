import copy
import tkinter as tk
import time
from FigureShape import FigureShape
from Brick import  Brick
from GameField import GameField
from Common import To

class App(tk.Tk):
    draw_time = 0  # интервал в мс с которым обновляется картинка на экране

    # Глобальные настройки игры
    brick_width = 1.
    brick_height = 1.
    scene_width = 10.
    scene_height = 2.*scene_width
    pixels_per_unit = 20.
    FPS = 30
    fall_speed = 4. # скорость падения фигуры в юнитах/сек

    test_figure : FigureShape = None
    figure_shift_per_frames = 0.
    frozen_bricks = None

    def __init__(self):
        super().__init__()

        self.set_FPS(self.FPS)

        self.update_idletasks()
        width = self.winfo_screenwidth()/2
        height = self.winfo_screenheight()*0.8
        self._canvas = tk.Canvas(self, width=width, height=height, bd=0, highlightthickness=0)
        self._canvas.pack()
        self.geometry(str(int(width)) + "x" + str(int(height)) +"+0+0")

        self.after(self.draw_time, self.game_loop)
        self.update()

        # TODO: разобраться как назначить обработку событий на нажатие определенных кнопок
        #self._canvas.bind_all('<Key>', self.user_input_handler)
        self._canvas.bind_all('<KeyPress>', self.on_key_press)
        self._canvas.bind_all('<KeyRelease>', self.on_key_release)

        self.rect = self._canvas.create_rectangle(0, 0, 50, 50, fill='red')
        self.initpos = 0
        self.test_figure = FigureShape(0, 0., 0., self.brick_width, self.brick_height, 1, [0., self.fall_speed])
        self.test_figure.move_vert_on(2.)
        self.test_figure.move_hor_on(2.)
        self.figure_shift_per_frames = 0.
        self.myBrick = Brick(2., 2., color='green')

        self.game_field = GameField(12., 25.)

        self.frozen_bricks = list()

    def set_FPS(self, FPS: int):
        self.draw_time = int(1000 / FPS)

    def on_key_press(self, event):
        if event.keysym == 'Left':
            self.move_figure(To.Left)

        elif event.keysym == 'Right':
            self.move_figure(To.Right)

        elif event.keysym == 'Down':
            self.move_figure(To.Bottom)

        return

    def on_key_release(self, event):
        if event.keysym == 'Up':
            self.rotate_figure()
        return

    def game_loop(self):
        self._canvas.delete('all') # очистка экрана
        #self.rect = self._canvas.create_rectangle(0, self.initpos, 50, 50 + self.initpos, fill='red')

        # Создаем новую случайную фигуру, если на экране нет падающих фигур
        self.create_new_figure()

        # Проверяем, не оказалась ли фигура за пределами экрана из-за пользовательского ввода.
        # Если оказалась, то откатываем ее положение назад

        # Перемещаем фигуру
        self.translate_figure_down()

        # Проверяем, не достигла ли фигура дна.
        if self.is_figure_on_bottom():
                print('figure is on bottom')
        #       Проверяем не выполняется ли условие на проигрыш
                if self.is_game_over():
                    return
                else:
        #           Помещаем фигуру в общий набор кубиков на дне
                    self.froze_figure_bricks()
        #           Удаляем фигуру
                    self.destroy_figure()
        #           Удаляем заполненные линии, добавляем игроку очки
                    self.clear_frozen_lines()

        #Отрисовываем всю сцену
        self.draw_scene()
        self.after(self.draw_time, self.game_loop)

    def is_game_over(self):
        return False

    def create_new_figure(self):
        if self.test_figure != None:
            #self.test_figure = FigureShape()
            return
        return

    def move_figure(self, dir: int):
        #Сохраняем положение фигуры
        figure_prev_state = self.test_figure.get_state()

        #Меняем положение фигуры
        if dir == To.Left:
            self.test_figure.move_hor_on(-self.brick_width)
        elif dir == To.Right:
            self.test_figure.move_hor_on(self.brick_width)
        elif dir == To.Bottom:
            self.test_figure.move_vert_on(self.brick_height)
        else:
            return

        #Проверяем, не выпадает ли фигура за пределы поля
        if self.is_figure_out_of_scene() == True:
            #Возвращаем фигуру в предыдущее положение
            self.test_figure.set_from_state(figure_prev_state)


    def rotate_figure(self):
        # Сохраняем положение фигуры
        figure_prev_state = self.test_figure.get_state()

        # Меняем положение фигуры
        self.test_figure.rotate_right()

        # Проверяем, не выпадает ли фигура за пределы поля
        if self.is_figure_out_of_scene() == True:
            # Возвращаем фигуру в предыдущее положение
            self.test_figure.set_from_state(figure_prev_state)

    def translate_figure_down(self):
        figure_speed = self.test_figure.get_speed()
        self.figure_shift_per_frames += figure_speed[1] * (float(self.draw_time) * 0.001)

        if self.figure_shift_per_frames >= self.brick_height:
            self.test_figure.move_vert_on(self.brick_height)
            self.figure_shift_per_frames = 0.
        return

    def is_figure_out_of_scene(self):
        scene_dims = self.game_field.get_dimensions()
        bricks = self.test_figure.get_bricks()
        for brick in bricks:
            if brick.is_brick_out_of_scene(scene_dims[0], scene_dims[1]) == True:
                return True
        return False

    def is_figure_on_bottom(self):
        scene_dims = self.game_field.get_dimensions()
        bricks = self.test_figure.get_bricks()
        for brick in bricks:
            if brick.is_brick_on_bottom(scene_dims[1]):
                return True
            else:
                for frozen_brick in self.frozen_bricks:
                    if brick.collide_test_with_brick(frozen_brick):
                        return True
        return False

    def froze_figure_bricks(self):
        bricks = self.test_figure.get_bricks()
        for brick in bricks:
            new_brick = copy.deepcopy(brick)
            new_brick.color = 'gray'
            self.frozen_bricks.append(new_brick)
            print('ADDED')
        return

    def destroy_figure(self):
        self.test_figure.set_xy(0.,0.)
        #TODO: разобраться, как уничтожить объект в питоне
        return

    def clear_frozen_lines(self):
        return

    def draw_scene(self):
        def draw_brick(self, brick: Brick):
            points = brick.get_points()
            print(points)
            self._canvas.create_rectangle(points[0][0] * self.pixels_per_unit, points[0][1] * self.pixels_per_unit,
                                          points[2][0] * self.pixels_per_unit, points[2][1] * self.pixels_per_unit,
                                          fill=brick.color)
            return

        def draw_game_field(self):
            # рисуем игровое поле
            x0 = 0.
            y0 = 0.
            game_field_dims = self.game_field.get_dimensions()
            self._canvas.create_rectangle(x0 * self.pixels_per_unit, y0 * self.pixels_per_unit,
                                          (x0 + game_field_dims[0]) * self.pixels_per_unit,
                                          (y0 + game_field_dims[1]) * self.pixels_per_unit, fill='white')
            return

        def draw_falling_figure(self):
            # рисуем падающую фигуру
            brickPoints = self.myBrick.get_points()
            self._canvas.create_rectangle(brickPoints[0][0] * self.pixels_per_unit,
                                          brickPoints[0][1] * self.pixels_per_unit,
                                          brickPoints[2][0] * self.pixels_per_unit,
                                          brickPoints[2][1] * self.pixels_per_unit,
                                          fill=self.myBrick.color)
            bricks = self.test_figure.get_bricks()
            for brick in bricks:
               draw_brick(self, brick)
            return

        def draw_frozen_bricks(self):
            for brick in self.frozen_bricks:
                draw_brick(self, brick)
            return

        draw_game_field(self)
        print('----------------------------------------------------------------------------')

        draw_frozen_bricks(self)
        draw_falling_figure(self)

        return

if __name__ == "__main__":
    app = App()
    app.mainloop()

# Для справки

# frame = tk.Frame(self, bg='green', height=100, width=100)
# frame.bind('<Right>', self.event_handler)
# frame.bind('<Left>', self.event_handler)
# frame.bind('<Up>', self.event_handler)
# frame.bind('<Down>', self.event_handler)
#
# frame.bind('<Enter>', self.event_handler)
# frame.pack(padx=50, pady=50)

# tk = Tk()
# canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()
#
# def on_arrows(event):
#     print('Key pressed: ', event.keysym)
#
# canvas.bind_all('<Key>', on_arrows)
# tk.mainloop()
