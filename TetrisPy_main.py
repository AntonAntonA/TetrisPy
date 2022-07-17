import tkinter as tk
import time
from FigureShape import FigureShape

class App(tk.Tk):
    draw_time = 0  # интервал в мс с которым обновляется картинка на экране

    # Глобальные настройки игры
    brick_width = 1.
    brick_height = 1.
    scene_width = 10.
    scene_height = 2.*scene_width
    pixels_per_unit = 30.
    FPS = 30
    fall_speed = 4. # скорость падения фигуры в юнитах/сек

    test_figure : FigureShape = None
    figure_shift_per_frames = 0.

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

    def set_FPS(self, FPS: int):
        self.draw_time = int(1000 / FPS)

    def on_key_press(self, event):
        if event.keysym == 'Left':
            self.test_figure.move_hor_on(-self.brick_width)

        elif event.keysym == 'Right':
            self.test_figure.move_hor_on(self.brick_width)

        elif event.keysym == 'Down':
            self.test_figure.move_vert_on(self.brick_height)
        return

    def on_key_release(self, event):
        if event.keysym == 'Up':
            self.test_figure.rotate_right()
        print(event.type)
        return

    def game_loop(self):
        self._canvas.delete('all') # очистка экрана
        #self.rect = self._canvas.create_rectangle(0, self.initpos, 50, 50 + self.initpos, fill='red')

        # Создаем новую случайную фигуру, если на экране нет падающих фигур
        #self.create_new_figure()

        # Проверяем, ввел ли пользователь что-то. Если ввел, то передаем этот ввод падающей фигуре
        #if self.user_input.is_user_input_valid() == True:
            # TODO:
         #   1 + 1
           # return

        # Проверяем, не оказалась ли фигура за пределами экрана из-за пользовательского ввода.
        # Если оказалась, то откатываем ее положение назад

        # Перемещаем фигуру
        self.move_figure()

        # Проверяем, не достигла ли фигура дна.
        # Если достигла:
        #       Проверяем не выполняется ли условие на проигрыш
        #       Помещаем фигуру в общий набор кубиков на дне
        #       Удаляем заполненные линии, добавляем игроку очки
        # Иначе:
        #        Идем на следующую итерацию игрового цикла

        #Отрисовываем всю сцену
        self.draw_scene()
        self.after(self.draw_time, self.game_loop)

    def create_new_figure(self):
        return

    def move_figure(self):
        figure_speed = self.test_figure.get_speed()
        self.figure_shift_per_frames += figure_speed[1] * (float(self.draw_time) * 0.001)

        if self.figure_shift_per_frames >= self.brick_height:
            self.test_figure.move_vert_on(self.brick_height)
            self.figure_shift_per_frames = 0.
        return

    def draw_scene(self):
        bricks = self.test_figure.get_bricks()
        print('----------------------------------------------------------------------------')
        for brick in bricks:
            points = brick.get_points()

            print(points)
            self._canvas.create_rectangle(points[0][0] * self.pixels_per_unit, points[0][1] * self.pixels_per_unit,
                                          points[2][0] * self.pixels_per_unit, points[2][1] * self.pixels_per_unit,
                                          fill='red')
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
