import tkinter as tk
import time
import UserInput


class App(tk.Tk):
    draw_time = 0  # интервал в мс с которым обновляется картинка на экране
    user_input: UserInput = UserInput.UserInput()

    def __init__(self):
        super().__init__()

        # Устанавливаем FPS в 30 кадров в секунду
        self.set_FPS(30)

        self.update_idletasks()
        width = self.winfo_screenwidth()/2
        height = self.winfo_screenheight()*0.8
        self._canvas = tk.Canvas(self, width=width, height=height, bd=0, highlightthickness=0)
        self._canvas.pack()
        self.geometry(str(int(width)) + "x" + str(int(height)) +"+0+0")

        self.after(self.draw_time, self.game_loop)
        self.update()

        # TODO: разобраться как назначить обработку событий на нажатие определенных кнопок
        self._canvas.bind_all('<Key>', self.user_input_handler)
        self._canvas.bind_all('<KeyRelease>', self.user_input_handler)

        self.rect = self._canvas.create_rectangle(0, 0, 50, 50, fill='red')
        self.initpos = 0

    def set_FPS(self, FPS: int):
        self.draw_time = int(1000 / FPS)

    def user_input_handler(self, event):
        self.initpos += 10
        print(event.type)

    def game_loop(self):
        self._canvas.delete('all') # очистка экрана
        self.initpos += 1
        self.rect = self._canvas.create_rectangle(0, self.initpos, 50, 50 + self.initpos, fill='red')
        # Создаем новую случайную фигуру, если на экране нет падающих фигур
        self.create_new_figure()

        # Проверяем, ввел ли пользователь что-то. Если ввел, то передаем этот ввод падающей фигуре
        if self.user_input.is_user_input_valid() == True:
            # TODO:
            1 + 1
           # return

        # Проверяем, не оказалась ли фигура за пределами экрана из-за пользовательского ввода.
        # Если оказалась, то откатываем ее положение назад

        # Перемещаем фигуру вниз

        # Проверяем, не достигла ли фигура дна.
        # Если достигла:
        #       Проверяем не выполняется ли условие на проигрыш
        #       Помещаем фигуру в общий набор кубиков на дне
        #       Удаляем заполненные линии, добавляем игроку очки
        # Иначе:
        #        Идем на следующую итерацию игрового цикла

        #Отрисовываем всю сцену
        self.draw_scene()
        self.after(self._draw_time, self.game_loop)

    def create_new_figure(self):
        return

    def draw_scene(self):
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
