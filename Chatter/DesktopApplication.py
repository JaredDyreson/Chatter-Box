"""
Desktop application for Chatter Box
Use as an import
"""

import tkinter
import Equations
import functools

class Application():
    def __init__(self):
        self.equation_handler = Equations.Generator()
        self.window = tkinter.Tk()
        self.window.geometry("200x200")
        self.generate_button = tkinter.Button(self.window, text="Generate Equation", command=self.hello)
        self.evaluate_button = tkinter.Button(self.window, text="Evaluate Equation", command=functools.partial(self.equation_handler.check, self.entry.get(), self.))

        self.generate_button.place(x=50, y=50)
        self.evaluate_button.place(x=50, y=100)

        tkinter.Label(self.window, text="Input: ").pack(side=tkinter.LEFT)

        self.entry = tkinter.Entry(self.window, bd = 5)
        self.entry.pack(side=tkinter.RIGHT)

    def run(self):
        try:
            self.window.mainloop()
        except KeyboardInterrupt:
            quit()

    def hello(self):
        print(Equations.Generator().equation())
        print(self.entry.get())

class Login():
    def __init__()
A = Application()
A.run()
