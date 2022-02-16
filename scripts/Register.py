import tkinter as tk
from tkinter import Tk, Label, messagebox, StringVar, IntVar, Entry, Button, Toplevel, Checkbutton
import mysql.connector
from config import password
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
        top = Toplevel()
        top.title("Registaration")
        top.geometry("500x450+400+25")
        self.email = StringVar()
        self.passwor = StringVar()
        self.checkButton = IntVar()
        self.check_value = 0
        self.pass_entry = None

        self.buttons(top)
        top.mainloop()

    def checkbox(self, root):
        self.check_value = self.checkButton.get()
        if self.check_value == 0:
            self.pass_entry.configure(show="*")
        else:
            self.pass_entry.configure(show="")
    
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
            import mysql.connector
            con = mysql.connector.connect(
                host="localhost", 
                user="root",
                password=password,
                database="register"
            )
            mycursor = con.cursor()
            sql_query = 'SELECT username FROM users'
            mycursor.execute(sql_query)
            used_email = mycursor.fetchall()
            for i in used_email:
                if emailid == i[0]:
                    check = False
            if check:
                error_list = []
                characters = '@#$'
                count = 0
                print()

                flag = 0
                flag1 = 0
                char_count = 0
                low_count = 0
                up_count = 0
                dig_count = 0
                n = len(passw)
                if n < 8:
                    flag1 = 1
                    messagebox.showerror(master=top,title="Error",message= "The password must be atleast 8 letters!")
                if n > 15:
                    flag1 = 1
                    messagebox.showerror(master=top,title="Error",message= "The password must be atmost 15 letters!")
                for x in passw:
                    if x.islower():
                        low_count = low_count + 1
                    elif x.isupper():
                        up_count = up_count + 1
                    elif x.isdigit():
                        dig_count = dig_count + 1
                    else:
                        for i in characters:
                            if i == x:
                                char_count = char_count + 1
                if dig_count < 1 :
                    messagebox.showerror(master=top,title="Error",message= "At least 1 number between [0-9]")
                    top.lift()
                    return
                if char_count < 1:
                    messagebox.showerror(master=top,title="Error",message= "At least 1 character from [$#@]")
                    top.lift()
                    return
                if low_count < 1:
                    messagebox.showerror(master=top,title="Error",message= "Atleast 1 lowercase letter is mandatory")
                    top.lift()
                    return
                if up_count < 1:
                    messagebox.showerror(master=top,title="Error",message= "Atleast 1 uppercase letter is mandatory")
                    
                if low_count < 1 or up_count < 1 or dig_count < 1 or char_count < 1:
                    flag1 = 1
                    for i in error_list:
                        print(i, end="\n")
                    print("Registration Unsuccessful")

                if flag1 == 0:
                    sql = 'INSERT INTO users (username, password) VALUES (%s, %s)'
                    val = (emailid, passw)
                    mycursor.execute(sql, val)
                    con.commit()
                    messagebox.showinfo(master=top,title="Registration successful",
                                        message="You have been registered successfully!")
                    top.destroy()
            else:
                messagebox.showwarning(master=top,title="Oops",message= "Email id already registered!")
                top.destroy()
                Register()

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