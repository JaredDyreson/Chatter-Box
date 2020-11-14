"""
Desktop application for Chatter Box
Use as an import
"""

import tkinter
import Equations
import functools
from Client import Client

class Popup():
    def __init__(self, equation: str):
        if not(isinstance(equation, str)):
            raise ValueError
        self.window = tkinter.Tk()
        self.window.geometry("100x100")
        self.equation = equation
        self.question_label = tkinter.Label(self.window, text=self.equation)
        self.question_label.pack(side=tkinter.RIGHT)
        self.response = tkinter.Entry(self.window)
        self.response.pack(side=tkinter.RIGHT)


    def run(self):
        try:
            self.window.mainloop()
            print("HELLL")
        except KeyboardInterrupt:
            quit()


class Application():
    def __init__(self):
        self.equation_handler = Equations.Generator()
        self.window = tkinter.Tk()
        self.window.geometry("200x200")
        self.equation = self.equation_handler
        self.subwindow = Popup("2+2")
        self.generate_button = tkinter.Button(self.window, text="Generate Equation", command=self.subwindow.run())

        # self.evaluate_button = tkinter.Button(self.window, text="Evaluate Equation", command=functools.partial(self.equation_handler.check, self.entry.get(), self.))

        self.generate_button.place(x=50, y=50)
        # self.evaluate_button.place(x=50, y=100)

        tkinter.Label(self.window, text="Input: ").pack(side=tkinter.LEFT)
        tkinter.Label(self.window, text="Jared").pack(side=tkinter.RIGHT)


    def run(self, client: Client):
        self.player = client
        try:
            self.window.mainloop()
        except KeyboardInterrupt:
            quit()

    def printer_(self):
        print("fuk")

    def generate_payload(self):
        return {
            "name": self.player.name,
            "answer": contents if contents else None
        }

    def eval_(self):
        eq = self.equation_handler.equation()
        answer = self.entry.get()

C1 = Client("Jared")
A = Application()
A.run(C1)
