import tkinter
from Chatter import Generator
from kevin import NumpadWindow


# Connection is global

G = Generator()

class MainWindow(tkinter.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
        self.button = tkinter.Button(self, text="Submit",
                                command=self.create_waiting_page)
        self.button.pack(side="top")
        self.parent = kwargs

    def create_numpad(self):
        self.counter += 1
        here = NumpadWindow(tkinter.Toplevel(self))

    def create_waiting_page(self):
        self.counter+=1
        WaitingRoom(tkinter.Toplevel(self))


class WaitingRoom():
    def __init__(self, win=None):
        self.window = tkinter.Tk() if not win else win
        self.window.geometry("300x300")
        self.label_ = tkinter.Label(self.window, text="Waiting room")
        self.label_.pack(side="top", padx=100, pady=100)


class Login():
    def __init__(self, win=None):
        self.window = tkinter.Tk() if not win else win
        self.window.geometry("300x300")

        self.user_name_label = tkinter.Label(self.window, text="Username:")
        self.user_name_label.pack(side="top", padx=100, pady=100)
        self.user_name_entry = tkinter.Entry(self.window)
        self.user_name_entry.pack(side="top")

    def run(self):
        self.window.mainloop()

L = Login()

main = MainWindow(L.window)

main.pack(side="top", fill="both", expand=True)
L.run()
