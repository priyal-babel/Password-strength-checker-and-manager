import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
from Register import Register
from Login import Login
from FullScreen import FullScreenApp

class Main:
    def __init__(self):
        root = Tk()
        FullScreenApp(root)
        root.title("Password checker and manager")
        self.buttons(root)
        root.mainloop()

    def userLogin(self):
        Login()

    def userRegister(self):
        Register()

    def buttons(self, root):
        but1 = Button(
            root,
            bd=0,
            relief="groove",
            compound=tk.CENTER,
            bg="white",
            fg="black",
            activeforeground="pink",
            activebackground="white",
            font="arial 12",
            text="Login",
            pady=10,
            borderwidth=10,
            height=1,
            width=30,
            command=self.userLogin
        )

        but1.place(x=600, y=300)
        but2 = Button(
            root,
            bd=0,
            relief="groove",
            compound=tk.CENTER,
            bg="white",
            fg="black",
            activeforeground="pink",
            activebackground="white",
            font="arial 12",
            text="Register",
            pady=10,
            borderwidth=10,
            height=1,
            width=30,
            command=self.userRegister
        )

        but2.place(x=600, y=400)


Main()