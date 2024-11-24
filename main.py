import tkinter
from Sign_In import Sign_In
from Sign_Up import Sign_Up


class Main:
    def __init__(self):
        self.root =tkinter.Tk()
        self.root.title("Password Manaager")
        self.root.geometry("800x400")
        self.root.config(bg="#000000")
        # self.root.resizable(False, False)
        in_frame = tkinter.Frame(self.root, width=800, height=90, bg="#000000")
        in_frame.pack()
        wel_label = tkinter.Label(in_frame, text="WELCOME! TO PASSWORD MANAGER", font=("Arial", 21, "bold"), bg="#000000", fg="#ffffff")
        wel_label.place(x=100, y=20)
        ui1_frame=tkinter.Frame(self.root, width=800, height="120", bg="#000000")
        ui1_frame.place(x=0, y=120)
        sign_up_button = tkinter.Button(ui1_frame, text="Sign Up", font=("Arial", 16, "bold"), bg="#274e13", fg="#ffffff", command=self.sign_up)
        sign_up_button.place(x=250, y=20)
        sign_in_button = tkinter.Button(ui1_frame, text="Sign In", font=("Arial", 16, "bold"), bg="#274e13", fg="#ffffff", command=self.sign_in)
        sign_in_button.place(x=400, y=20)
        self.root.mainloop()

    def sign_up(self):
        self.root.destroy()
        Sign_Up()

    def sign_in(self):
        self.root.destroy()
        Sign_In()




if __name__ == '__main__':
    Main()


