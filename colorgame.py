import time
from tkinter import messagebox
from tkinter import *
import random 

class colorgame(Tk):
    def __init__(self):
        super().__init__() 
        self.title("Basic Color Game")
        self.resizable(width=False, height=False)
        #self.configure(background = 'black')
        self.createWidget()
        self.color = ['red', 'blue', 'green', 'pink', 'black',
                         'yellow', 'orange', 'purple', 'brown', "white", "cyan"]

    def createWidget(self):
        self.timeLeft = 60
        self.Score = 0
        self.timer = Label(self, text="Time Left: 60", font="Brice 20")
        self.timer.grid(column=0, row=0)

        self.score = Label(self, text="Score: 0", font="Brice 20") 
        self.score.grid(column=2, row=0)

        self.display = Label(self, text="Start/Enter to Play", font="Brice 40", fg="White")
        self.display.grid(column=1, row=1)

        self.answer = Entry(self, font="Brice 20")
        self.answer.grid(column=1, row=2) 
        self.answer.insert(0, "Click start to start")
        self.answer.focus()
        
        self.btn = Button(self, text="Start", font="Brice 20", command=self.startGame)
        self.btn.grid(column=1, row=3)
        self.bind('<Return>', self.startGame)

    def startGame(self, Event=None):
        if self.timeLeft == 60:
            self.answer.delete(0, END) 
            self.countdown() 
        self.nextColor() 

    def nextColor(self): 
        self.answer.focus_set()
        n = self.answer.get().lower()
        if n == self.color[2].lower():
            self.Score += 1
            _score = "Score: %2d" % self.Score
            self.score.configure(text=_score)

        self.answer.delete(0, END)
        random.shuffle(self.color) 

        self.display.configure(fg=str(self.color[2]), bg=str(self.color[1]), text=str(self.color[0])) 

    def countdown(self):
        if self.timeLeft > 0:
            self.timeLeft -= 1
            self.timer.configure(text="Time Left: " + str(self.timeLeft))
            self.after(1000, self.countdown)
        else:
            self.createWindow() 

    def createWindow(self):
        self.mess = messagebox.askquestion(
            "Time out!!!", "Your score is: " + str(self.score) + "\nDo you want to restart?")
        if self.mess == "yes":
            self.createWidget()
        else:
            self.destroy() 

game = colorgame()
game.mainloop()
