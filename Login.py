from tkinter import Button, Checkbutton, Entry, IntVar, Label, StringVar, Tk, Toplevel, messagebox 
from Register import Register
import MySQLdb

class Login:
    def __init__(self):
        root = Toplevel()
        # root = Tk()
        root.title("Login")
        root.geometry("400x300")

        self.email = StringVar()
        self.passwor = StringVar()
        self.checkButton = IntVar()
        self.check_value = 0
        self.pass_entry = None

        self.buttons(root)
        root.mainloop()

    def callback(self,root):
        root.destroy()
        Register()

    def checkbox(self, root):
        self.check_value = self.checkButton.get()
        if self.check_value == 0:
            self.pass_entry.configure(show="*")
        else:
            self.pass_entry.configure(show="")

    def database(self,root):
        if self.email.get()=='':
            messagebox.showerror(master=root,title="Form Empty", message="Please enter email id!")
            root.lift()
            return
        try:
            con = MySQLdb.connect(host='localhost', user="user",
                                  password="password", database="")
            cursor = con.cursor()
            command = 'SELECT emailid,password FROM registration'
            cursor.execute(command)
            registered_email = cursor.fetchall()
            for each in registered_email:
                if each[0]==self.email.get():
                    if each[1]==self.passwor.get():
                        messagebox.showinfo(master=root,title="Welcome",message="You have been logged in!")
                        root.destroy()
                        # PastBookings(self.email.get())
                        return
                    else:
                        messagebox.showerror(master=root,title="",message="Incorrect password")
                        root.lift()
                        return
            messagebox.showwarning(master=root,title="Please register",message="Email id not registered. Register now!")
            root.lift()

        except Exception as e:
            print(e)
            messagebox.showerror(master=root,title="Error",message= "Error\nUnable to login.")
            root.lift()

    def buttons(self, root):
        Label(root, text="Login", font=("Times New Roman", 25,'bold')).place(x=150, y=20)

        Label(root, text="Email:", font=("Times New Roman", 15)).place(x=50,y=100)
        Entry(root, width=30, textvar=self.email).place(x=150, y=105)
        
        Checkbutton(root, text = "Show password", 
                      variable = self.checkButton,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command = lambda: self.checkbox(root)).place(x=150,y=175)
        Label(root, text="Password:", font=("Times New Roman", 15)).place(x=50, y=150)
        self.pass_entry = Entry(root, width=30,textvar=self.passwor,show="*")
        self.pass_entry.place(x=150, y=155)

        Button(root, text='Submit', width=15, height=1, bg='brown', fg='white', command=lambda: self.database(root)).place(x=140, y=230)
        
        Label(root, text="Not a registered user?", font=("Times New Roman", 10)).place(x=90,y=260)

        link = Label(root, text="Register Now!", fg="blue", cursor="hand2")
        link.place(x=215,y=260)
        link.bind("<Button-1>", lambda e: self.callback(root))