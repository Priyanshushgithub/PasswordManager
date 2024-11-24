import tkinter
from tkinter import messagebox
import mysql.connector
import Window


class Sign_Up:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="lenovo", database="DBMS_Projects")
        self.cursor = self.conn.cursor()

        self.root = tkinter.Tk()
        self.root.geometry("650x490")
        self.root.title("Password Manager")
        self.root.config(bg="#000000")

        sign_up_frame = tkinter.Frame(self.root, width=450, height=400, bg="#ffffff")
        sign_up_frame.place(x=100, y=40)

        su_label = tkinter.Label(sign_up_frame, text="SIGN UP", font=("Ojuju", 18, "bold"), fg="#000000")
        su_label.place(x=180, y=40)

        self.name_label = tkinter.Label(sign_up_frame, text="Name", font=("Ojuju", 12, "bold"), bg="#ffffff", fg="#000000")
        self.name_label.place(x=40, y=90)

        self.name_entry = tkinter.Entry(sign_up_frame, font=("Ojuju",12), bg="#ffffff")
        self.name_entry.place(x=40, y=120)

        self.email_label = tkinter.Label(sign_up_frame, text="Email Address", font=("Ojuju", 12, "bold"))
        self.email_label.place(x=40, y=160)

        self.email_entry = tkinter.Entry(sign_up_frame, font=("Ojuju",12), bg="#ffffff")
        self.email_entry.place(x=40, y=190)

        self.password_label = tkinter.Label(sign_up_frame, text="Password", font=("Ojuju", 12, "bold"))
        self.password_label.place(x=40, y=210)

        self.password_entry = tkinter.Entry(sign_up_frame, font=("Ojuju", 12), bg="#ffffff")
        self.password_entry.place(x=40, y=240)

        register_Button = tkinter.Button(sign_up_frame, text="Register", font=("Arial", 18, "bold"), bg="#274e13", fg="#ffffff", command=self.Register)
        register_Button.place(x=180, y=280)

        self.root.mainloop()

    def Register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.cursor.execute("SELECT Email_Address FROM User_Details")
        data = self.cursor.fetchall()
        print(data)
        if email in data:
            messagebox.showerror(title="ERROR!!!!", message="USER NAME EXISTS")
        else:
            self.cursor.execute("Insert into User_Details(Name, Email_Address, Password) values('{0}', '{1}', '{2}')".format(name, email, password))
            self.conn.commit()
            self.root.destroy()
            self.conn.close()
            Window.Window(email)