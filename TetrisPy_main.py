import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        frame = tk.Frame(self, bg='green', height=100, width=100)
        frame.bind('<Right>', self.event_handler)
        frame.bind('<Left>', self.event_handler)
        frame.bind('<Up>', self.event_handler)
        frame.bind('<Down>', self.event_handler)

        frame.bind('<Enter>', self.event_handler)
        frame.pack(padx=50, pady=50)

    def event_handler(self, event):
        position = "(x={}, y={})".format(event.x, event.y)
        print(event.type, 'event', position)

if __name__ == "__main__":
    app = App()
    app.mainloop()


tk = Tk()
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

def on_arrows(event):
    print('Key pressed: ', event.keysym)

canvas.bind_all('<Key>', on_arrows)
tk.mainloop()


