# 🔐 Password Manager

A desktop-based **Password Manager** application developed using **Python**, **Tkinter**, and **MySQL**. The application allows users to register, log in securely, and manage passwords for different websites and applications through a simple graphical user interface.

---

# 📌 Features

* User Registration (Sign Up)
* User Authentication (Sign In)
* Save passwords for multiple applications
* Search saved passwords
* Update existing passwords
* Delete stored passwords
* MySQL database integration
* Simple and user-friendly Tkinter GUI

---

# 🛠️ Technologies Used

* Python 3.x
* Tkinter
* MySQL
* MySQL Connector for Python

---

# 📂 Project Structure

```
Password-Manager/
│
├── main.py          # Main application
├── Sign_Up.py       # User registration
├── Sign_In.py       # User login
├── Window.py        # Password Manager dashboard
├── README.md
```

---

# 🗄️ Database Setup

## Step 1: Create Database

```sql
CREATE DATABASE password_manager;
USE password_manager;
```

---

## Step 2: Create User_Details Table

```sql
CREATE TABLE User_Details (
    User_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email_Address VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);
```

---

## Step 3: Create Passwords Table

```sql
CREATE TABLE Passwords (
    Password_ID INT AUTO_INCREMENT PRIMARY KEY,
    Email_Address VARCHAR(100) NOT NULL,
    Social_App_Name VARCHAR(100) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    FOREIGN KEY (Email_Address)
        REFERENCES User_Details(Email_Address)
        ON DELETE CASCADE
);
```

---

# 🗂️ Database Relationship

```
                User_Details
             --------------------
             User_ID (PK)
             Name
             Email_Address (UNIQUE)
             Password
                    │
                    │ 1
                    │
                    ▼
                 Passwords
             --------------------
             Password_ID (PK)
             Email_Address (FK)
             Social_App_Name
             Password
```

One registered user can store multiple application passwords.

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/password-manager.git
```

Navigate to the project folder.

```bash
cd password-manager
```

Install the required package.

```bash
pip install mysql-connector-python
```

---

# ⚙️ Configure Database

Update the MySQL credentials in the following files:

* `Sign_Up.py`
* `Sign_In.py`
* `Window.py`

Replace:

```python
host="localhost"
user="root"
passwd="YOUR_PASSWORD"
database="password_manager"
```

with your own MySQL configuration.

---

# ▶️ Running the Project

Run the main file:

```bash
python main.py
```

---

# 🚀 Application Workflow

1. Launch the application.
2. Register a new account using **Sign Up**.
3. Log in using your registered email and password.
4. Save passwords for different applications.
5. Search, update, or delete saved passwords whenever needed.

---

# 📸 Screenshots

You can add screenshots here.

```
screenshots/
│
├── Home.png
├── SignUp.png
├── SignIn.png
├── Dashboard.png
└── Search.png
```

---

# 🔒 Current Functionality

* User Registration
* User Login
* Store Application Passwords
* Retrieve Stored Passwords
* Update Passwords
* Delete Passwords
* MySQL Database Connectivity
* Tkinter-Based GUI

---

# 🔮 Future Enhancements

* Encrypt stored passwords using AES/Fernet
* Hash login passwords using bcrypt
* Password Generator
* Password Strength Checker
* Copy password to clipboard
* Show/Hide password option
* Export passwords to CSV
* Import passwords
* Dark Mode
* Forgot Password functionality
* Multi-user session management

---

# 📚 Learning Outcomes

This project helped in understanding:

* Python GUI Development using Tkinter
* CRUD Operations
* MySQL Database Connectivity
* User Authentication
* Event-Driven Programming
* Database Relationships
* Exception Handling
* Object-Oriented Programming (OOP)

---

# ⚠️ Known Limitations

The current version is intended for learning purposes.

* Passwords are stored in plain text.
* SQL queries use string formatting instead of parameterized queries.
* No password encryption.
* No password hashing.
* No password recovery feature.

---

# 💡 Suggested Improvements

For a production-ready application:

* Use parameterized SQL queries to prevent SQL Injection.
* Hash user passwords using `bcrypt`.
* Encrypt stored passwords using `cryptography`.
* Add password strength validation.
* Implement session management.
* Add backup and restore functionality.
* Improve UI/UX with modern themes.

---

# 👨‍💻 Author

**Priyanshu Sharma**

* Python Developer
* Data Analyst
* Machine Learning Enthusiast
