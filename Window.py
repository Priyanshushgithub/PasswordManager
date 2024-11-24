import tkinter
from tkinter import messagebox
import mysql.connector


class Window:
    def __init__(self, email):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="PASSWORD", database="DATABASE_NAME")
        self.cursor = self.connection.cursor()
        self.root = tkinter.Tk()
        self.root.title("Password Manager")
        self.root.configure(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 400
        window_height = 400

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

            # self.obj.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.label_heading = tkinter.Label(self.root, text="Password Manager", font=("Arial", 16, "bold"), fg="white", bg="black")
        self.label_heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.Email_Address = email

        # self.label_email = tkinter.Label(self.root, text="Email Address:", font=("Arial", 12, "bold"), fg="white", bg="black")
        # self.label_email.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        # self.entry_email = tkinter.Entry(self.root, font=("Arial", 12))
        # self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        self.label_app = tkinter.Label(self.root, text="App Name:", font=("Arial", 12, "bold"), fg="white",
                                         bg="black")
        self.label_app.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_app = tkinter.Entry(self.root, font=("Arial", 12))
        self.entry_app.grid(row=1, column=1, padx=10, pady=5)


        self.label_password = tkinter.Label(self.root, text="Password:", font=("Arial", 12, "bold"), fg="white", bg="black")
        self.label_password.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_password = tkinter.Entry(self.root, show="*", font=("Arial", 12))
        self.entry_password.grid(row=2, column=1, padx=10, pady=5)

        self.button_save = tkinter.Button(self.root, text="Save", command=self.save_password, font=("Arial", 12, "bold"), bg="#008000", fg="white")
        self.button_save.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.button_update = tkinter.Button(self.root, text="Update", command=self.update_password, font=("Arial", 12, "bold"), bg="#0000ff", fg="white")
        self.button_update.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.button_search = tkinter.Button(self.root, text="Search", command=self.search_password, font=("Arial", 12, "bold"), bg="#ffa500", fg="black")
        self.button_search.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.button_delete = tkinter.Button(self.root, text="Delete", command=self.delete_password,
                                       font=("Arial", 12, "bold"), bg="#ff0000", fg="white")
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    def save_password(self):
        email = self.Email_Address
        app = self.entry_app.get()
        password = self.entry_password.get()

        if email and app and password:
            self.cursor.execute("INSERT INTO Passwords(Email_Address, Social_App_Name, Password) VALUES ('{0}', '{1}', '{2}')".format (email, app, password))
            self.connection.commit()
            messagebox.showinfo("Success", "Password saved successfully.")
        else:
            messagebox.showerror("Error", "Please enter email and App name and password.")

    def update_password(self):
        email = self.Email_Address
        app = self.entry_app.get()
        password = self.entry_password.get()

        if email and app and password:
            self.cursor.execute("UPDATE Passwords SET password='{0}' WHERE Email_Address='{1}' and Social_App_Name='{2}'".format(password, email, app))
            self.connection.commit()
            messagebox.showinfo("Success", "Password updated successfully.")
        else:
            messagebox.showerror("Error", "Please enter both account and password.")

    def search_password(self):
        email = self.Email_Address
        app = self.entry_app.get()

        if email and app:
            self.cursor.execute("SELECT Password FROM Passwords WHERE Email_Address='{0}' and Social_App_Name='{1}'".format(email, app))
            result = self.cursor.fetchone()
            if result:
                messagebox.showinfo("Password", f"The password for {app} is: {result[0]}")
            else:
                messagebox.showerror("Error", "No password found for the specified account.")
        else:
            messagebox.showerror("Error", "Please enter an account.")

    def delete_password(self):
        email = self.Email_Address
        app = self.entry_app.get()

        if email and app:
            self.cursor.execute("DELETE FROM Passwords WHERE Email_Address='{0}' and Social_App_Name='{1}'".format(email, app))
            self.connection.commit()
            messagebox.showinfo("Success", "Password deleted successfully.")
        else:
            messagebox.showerror("Error", "Please enter an account.")
