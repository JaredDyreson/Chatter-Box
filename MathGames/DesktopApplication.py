"""
Desktop application components for MathGames Box
Use as an import
"""

import tkinter
import socket
import threading
import time
import json
import select
import websocket

import tkinter.font
import tkinter.messagebox
from MathGames.Mixer import Mixer

background_color = "skyblue1"
button_color = "skyblue1"

h1_font = "Arial"
prev_score = 0

class Login():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Login")
        self.window.geometry("300x300")
        self.name = None
        self.window.resizable(width = False, height = False)

        login_background = tkinter.PhotoImage(file = "MathGames/assets/login.png")
        self.background = tkinter.Label(self.window, image = login_background)
        self.background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.background.image = login_background


        self.user_name_label = tkinter.Label(self.window, text="What is your name?", font=(32))
        self.user_name_label.pack(side="top", padx=50, pady=100)
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

class ConnectionFailed():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.withdraw()

    def run(self):
        tkinter.messagebox.showerror("Connection failed", "[-] Server is not active, please turn it on")

class NumpadWindow():
    def __init__(self, GameInstance, client):


        # DIMENSIONS

        self.window_width = 400
        self.window_height = 550
        self.win_count = 0
        self.client = client

        self.main_window = tkinter.Tk()

        self.main_window.title("Math Game")
        self.main_window.resizable(width = False, height = False)
        self.main_window.configure(width = self.window_width, height = self.window_height)

        self.message = ""
        self.gameInstance = GameInstance
        self.payload = json.loads(self.gameInstance.connection.recv())
        self.leader_board = self.payload["score_board"]
        self.equation = self.payload["question"]


        main_background = tkinter.PhotoImage(file = "MathGames/assets/background.png")
        self.mbackground = tkinter.Label(self.main_window, image = main_background)
        self.mbackground.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.mbackground.image = main_background

        self.timerCounter = tkinter.StringVar()
        self.timerCounter.set(f'Time: 0')

        self.winningCountMessage = tkinter.StringVar()
        self.winningCountMessage.set(f'You have won {self.win_count} times')
        self.currentAnswerMessage = tkinter.StringVar()
        self.currentAnswerMessage.set(f'Current answer: {self.message}')
        self.currentEquationMessage = tkinter.StringVar()
        self.currentEquationMessage.set(f'Current equation: {self.equation}')

        self.waitingLabel = tkinter.Label(self.main_window, textvariable = self.timerCounter, font = "100")
        self.waitingLabel.place(relwidth = 1, y = 20)
        self.waitingLabel.configure(bg=background_color)

        self.wincountLabel = tkinter.Label(self.main_window, textvariable = self.winningCountMessage, font = "100")
        self.wincountLabel.place(relwidth = 1)
        self.wincountLabel.configure(bg=background_color)

        self.currentResponse = tkinter.Label(self.main_window, textvariable = self.currentAnswerMessage, font = "100")
        self.currentResponse.place(relwidth = 1, y = 40)
        self.currentResponse.configure(bg=background_color)

        self.questionLabel = tkinter.Label(self.main_window, textvariable = self.currentEquationMessage, font = "100")
        self.questionLabel.place(relwidth = 1, y = 60)
        self.questionLabel.configure(bg=background_color)

        # BUTTON SETTINGS

        self.numpadVerticalOffset = 100
        self.numpadButtonHeight = 50
        self.numpadButtonFont = "14"
        self.numpadButtonWidth = self.window_width / 3

        buttons = [self.make_button(element) for element in range(1, 10)]
        buttons.append(self.make_button(0))

        self.submit_button = tkinter.Button(self.main_window, text="Submit", bg=button_color, command = self.send_func)
        self.delete_button = tkinter.Button(self.main_window, text="Delete", bg=button_color, command = self.delete_last_char)
        x_pos, y_pos = 0, 0
        for x, button in enumerate(buttons):
            if(x % 3 == 0 and x > 0):
                x_pos = 0
                y_pos+=1
                if y_pos == 3:
                    x_pos = 1
            button.place(x = x_pos * self.numpadButtonWidth if x_pos > 0 else x_pos,
                         y = self.numpadVerticalOffset + (self.numpadButtonHeight * y_pos),
                         width = self.numpadButtonWidth,
                         height = self.numpadButtonHeight
                        )
            x_pos+=1

        self.submit_button.place(x = 0,
                                 y = self.numpadVerticalOffset + self.numpadButtonHeight * (y_pos + 1),
                                 width = self.numpadButtonWidth,
                                 height = self.numpadButtonHeight
                                )
        self.delete_button.place(x = self.numpadButtonWidth,
                                 y = self.numpadVerticalOffset + self.numpadButtonHeight * (y_pos + 1),
                                 width = self.numpadButtonWidth,
                                 height = self.numpadButtonHeight
                                )
        self.previous_leaderboard = json.loads(self.gameInstance.connection.recv())["score_board"]
        self.music = Mixer()
        self.did_win = None
        self.can_make_sound = False

        main_splashscreen = tkinter.PhotoImage(file = "MathGames/assets/win_splash.png")
        self.msplash = tkinter.Label(self.main_window, image = main_splashscreen)
        self.msplash.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.msplash.image = main_splashscreen
        self.hide_win_screen()

        loss_splashscreen = tkinter.PhotoImage(file = "MathGames/assets/loss_splash.png")
        self.lsplash = tkinter.Label(self.main_window, image = loss_splashscreen)
        self.lsplash.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.lsplash.image = loss_splashscreen
        self.hide_loss_screen()
        




    def display_win_screen(self, time=1000):    
        self.show_win_screen()
        self.msplash.after(time, self.hide_win_screen)

    def display_loss_screen(self, time=1000):
        self.show_loss_screen()
        self.lsplash.after(time, self.hide_loss_screen)

    def hide_win_screen(self):
        self.msplash.lower()

    def show_win_screen(self):
        self.msplash.lift()

    def hide_loss_screen(self):
        self.lsplash.lower()
    
    def show_loss_screen(self):
        self.lsplash.lift()
    

    def make_button(self, index):
        filepath = f'MathGames/assets/button{index}.png'
        button_image = tkinter.PhotoImage(file=filepath)
        b = tkinter.Button(self.main_window, font = self.numpadButtonFont, image=button_image, text = str(index), border=0, command = lambda : self.append_message(str(index)))
        b.image = button_image
        return b

    def run(self):
        self.updater()
        self.main_window.mainloop()

    def updater(self):
        self.refresh_screen()
        self.main_window.after(1000, self.updater)

    def kill(self):
        self.gameInstance.connection.close()
        self.main_window.destroy()

    def append_message(self, message):
        self.message+=message
        self.currentAnswerMessage.set(f'Current answer: {self.message}')

    def delete_last_char(self):
        if not(self.message):
            return
        container = list(self.message)
        container.pop()
        self.message = ''.join(container)
        self.currentAnswerMessage.set(f'Current answer: {self.message}')

    def send_func(self):
        if not(self.message):
            return
        try:
            _ = int(self.message)
        except ValueError:
            return

        outbound = {
            "name": self.client.name,
            "answer": self.message
        }
        
        dumped = json.dumps(outbound)
        try:
            self.gameInstance.connection.send(dumped)
            self.did_win = eval(self.equation) == int(self.message)
            if(self.did_win):
                self.music.playHappy()
                self.display_win_screen(2000)
                print("you got it!")
            else:
                self.music.playSad()
                self.display_loss_screen(1000)
                print("uh oh!")
            self.did_win = False
            self.refresh_screen(can_wipe=True)
        except BrokenPipeError:
            print("[-] Connection has ended, re-establish connection")

            self.gameInstance.connection = self.gameInstance.establish_connection()




    def refresh_screen(self, can_wipe=False):
        if not(self.message):
            self.can_make_sound = False
        payload = json.loads(self.gameInstance.connection.recv())
        print(payload)
        leader_board = payload["score_board"]
        self.timerCounter.set(f'Time: {payload["time_out"]}')
        win_count = 0 if not self.client.name in leader_board else leader_board[self.client.name]

        self.equation = payload["question"]
        self.winningCountMessage.set(f'You have won {win_count} times')
        self.currentEquationMessage.set(f'Current equation: {self.equation}')

        if (can_wipe):
            while(self.message):
                self.delete_last_char()
