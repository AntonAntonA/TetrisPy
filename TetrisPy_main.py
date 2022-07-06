import tkinter as tk
import time
import UserInput

class App(tk.Tk):
    _draw_time = 33 # интервал в мс с которым обновляется картинка на экране
    user_input: UserInput = UserInput()

    def __init__(self):
        super().__init__()

        self.set_FPS(30)

        #TODO: Получить размеры экрана и сделать окно высотой в экран и щириной в половину экрана
        _canvas = tk.Canvas(self, width=500, height=500, bd=0, highlightthickness=0)
        _canvas.pack()

        self.after(self._draw_time, self.game_loop)
        self.update()

        #TODO: разобраться как назначить обработку событий на нажатие определенных кнопок
        _canvas.bind_all('<Key>', self.user_input_handler)
        _canvas.bind_all('<KeyRelease>', self.user_input_handler)

    def set_FPS(self, FPS: int):
        self._draw_time = int(1000 / FPS)

    def user_input_handler(self, event):
        print(event.type)

    def game_loop(self):
        # Создаем новую случайную фигуру, если на экране нет падающих фигур
        self.create_new_figure()

        # Проверяем, ввел ли пользователь что-то. Если ввел, то передаем этот ввод падающей фигуре
        if self.user_input.is_user_input_valid() == True:
            #TODO:
            return

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

        self.after(self._draw_time, self.game_loop)

if __name__ == "__main__":
    app = App()
    app.mainloop()


#Для справки

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


