import tkinter as tk
from tkinter import Tk, Label, messagebox, StringVar, IntVar, Entry, Button, Toplevel, Checkbutton
from password_strength import PasswordPolicy
import MySQLdb

class BLabel(object):
    b = "•"

    def __init__(self, master):
        self.l = tk.Label(master)

    def add_option(self, text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b+" "+text)
        else:
            self.l.config(text=self.l.cget("text") + "\n" + self.b + " "+text)


class Register:
    def __init__(self):
        top = Tk()
        top.title("Registaration")
        top.geometry("500x450+400+25")
        self.email = StringVar()
        self.passwor = StringVar()
        self.checkButton = IntVar()

        self.buttons(top)
        top.mainloop()

    def checkbox(self, root):
        self.check_value = self.checkButton.get()
        if self.check_value == 0:
            self.entry_6.configure(show="*")
        else:
            self.entry_6.configure(show="")
    
    def callback(self,top):
        from Login import Login
        top.destroy()
        Login()

    def isFormEmpty(self):
        if(self.email.get() == '' or self.passwor == ''):
            return True

    def database(self, top):
        check = True
        emailid = self.email.get()
        passw = self.passwor.get()
        if self.isFormEmpty() == True:
            messagebox.showerror(master=top,title="Form Empty",message= "Please enter all details!")
            top.lift()
            return
        if '@' not in emailid:
            messagebox.showerror(master=top,title="Error",message= "Invalid Email")
            top.lift()
            return

        try:
            # Password checker goes here
            x = 0
            policy = PasswordPolicy.from_names(
                length=8,  # min length: 8
                uppercase=2,  # need min. 2 uppercase letters
                numbers=2,  # need min. 2 digits
                special=2,  # need min. 2 special characters
                nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
            )
            policy.test(passw)
            if policy.test(passw) == []:
                top.lift()
            # Database goes here
            # cursor.execute("INSERT INTO registration VALUES(%s,%s)",
            #                        (emailid, passw))
            # con.commit()
            # messagebox.showinfo(master=top,title="Registration successful",
            #                     message="You have been registered successfully!")
            # top.destroy()
            # from Login import Login
            # Login()

        except Exception as e:
            print(e)
            messagebox.showerror(master=top,title="Error",message= "Error\nUnable to register.")
            top.lift()

    def buttons(self, top):
        label_0 = Label(top, text="Registration Form",
                        width=20, font=("Times New Roman", 25))
        label_0.place(x=75, y=23)

        Label(top, text="Email:", font=("Times New Roman", 15)).place(x=70,y=100)
        Entry(top, width=40, textvar=self.email).place(x=170, y=105)
        
        Checkbutton(top, text = "Show password", 
                      variable = self.checkButton,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command = lambda: self.checkbox(top)).place(x=170,y=175)
        Label(top, text="Password:", font=("Times New Roman", 15)).place(x=70, y=150)
        self.pass_entry = Entry(top, width=40,textvar=self.passwor,show="*")
        self.pass_entry.place(x=170, y=155)

        Lb1 = BLabel(master=top)
        Lb1.add_option("At least 1 letter between [a-z]")
        Lb1.add_option("At least 1 number between [0-9]")
        Lb1.add_option("At least 1 letter between [A-Z]")
        Lb1.add_option("At least 1 special character")
        Lb1.add_option("Minimum length of password: 8")
        Lb1.add_option("Maximum length of password: 15")
        Lb1.l.place(x=155, y=215)
        

        Button(top, text='Submit', width=20, height=2, bg='brown',
               fg='white', command=lambda: self.database(top)).place(x=180, y=330)
        Label(top, text="Have an account already?", font=("Times New Roman", 10)).place(x=150,y=380)

        link = Label(top, text="Login!", fg="blue", cursor="hand2")
        link.place(x=300,y=380)
        link.bind("<Button-1>", lambda e: self.callback(top))