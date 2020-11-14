"""
Desktop application components for Chatter Box
Use as an import
"""

import tkinter

class Login():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Login")
        self.window.geometry("300x300")
        self.name = None

        self.user_name_label = tkinter.Label(self.window, text="Username:")
        self.user_name_label.pack(side="top", padx=100, pady=100)
        self.user_name_entry = tkinter.Entry(self.window)
        self.user_name_entry.pack(side="top")
        self.submit_button = tkinter.Button(self.window, text = "Submit", command = self.name_)
        self.submit_button.pack(side="top")

    def run(self):
        self.window.mainloop()

    def name_(self):
        self.name = self.user_name_entry.get()
        if not(self.name):
            return
        self.window.destroy()
