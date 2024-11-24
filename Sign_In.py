import tkinter
from tkinter import messagebox
import mysql.connector
import Window


class Sign_In:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="PASSWORD", database="DATABASE_NAME")
        self.cursor = self.conn.cursor()

        self.root = tkinter.Tk()
        self.root.geometry("650x490")
        self.root.title("Password Manager")
        self.root.config(bg="#000000")

        sign_in_frame = tkinter.Frame(self.root, width=450, height=400, bg="#ffffff")
        sign_in_frame.place(x=100, y=40)

        si_label = tkinter.Label(sign_in_frame, text="SIGN IN", font=("Ojuju", 18, "bold"))
        si_label.place(x=180, y=40)

        self.email_label = tkinter.Label(sign_in_frame, text="Email Address", font=("Ojuju", 12, "bold"))
        self.email_label.place(x=40, y=90)

        self.email_entry = tkinter.Entry(sign_in_frame, font=("Ojuju", 12), bg="#ffffff")
        self.email_entry.place(x=40, y=120)

        self.password_label = tkinter.Label(sign_in_frame, text="Password", font=("Ojuju", 12, "bold"))
        self.password_label.place(x=40, y=160)

        self.password_entry = tkinter.Entry(sign_in_frame, font=("Ojuju", 12), bg="#ffffff")
        self.password_entry.place(x=40, y=190)

        login_Button = tkinter.Button(sign_in_frame, text="Log In", font=("Arial", 18, "bold"), bg="#274e13", fg="#ffffff", command=self.Login)
        login_Button.place(x=180, y=240)

        self.root.mainloop()

    def Login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.cursor.execute("select * from User_details where Email_Address='{0}' and Password='{1}'".format(email, password))
        d=self.cursor.fetchall()
        count = self.cursor.rowcount
        if count==0:
            messagebox.showinfo(title="ERROR", message="Enter invalid username and password")
        else:
            self.root.destroy()
            Window.Window(email)
