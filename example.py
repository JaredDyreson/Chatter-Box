import tkinter
from Chatter import Generator

# Connection is global

G = Generator()

class MainWindow(tkinter.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
        self.button = tkinter.Button(self, text="Generate Equation",
                                command=self.create_window)
        self.button.pack(side="top")

    def create_window(self):
        self.counter += 1
        t = tkinter.Toplevel(self)
        print(type(t))
        t.wm_title("Answer Window")
        l = tkinter.Label(t, text=f'{G.equation()}')
        entry = tkinter.Entry(t)
        submit = tkinter.Button(t, text="Submit")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        # entry.pack(side="top", expand=True, padx=100, pady=200)
        # submit.pack(side="top", expand=False, padx=100, pady=200)


class Application():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("200x200")

    def run(self):
        try:
            self.window.mainloop()
        except KeyboardInterrupt:
            quit()

A = Application()
main = MainWindow(A.window)

main.pack(side="top", fill="both", expand=True)
A.run()
