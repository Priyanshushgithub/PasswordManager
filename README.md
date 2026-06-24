# 🔐 Password Manager

A secure desktop-based Password Manager application developed using **Python**, **Tkinter**, and **MySQL**. The application allows users to securely store, manage, and retrieve login credentials for different websites and applications through an easy-to-use graphical interface.

---

## 📌 Features

- User-friendly GUI built with Tkinter
- Secure login system
- Add new website credentials
- View saved passwords
- Update existing credentials
- Delete stored credentials
- Search passwords by website name
- MySQL database integration
- Input validation and error handling

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (GUI)
- MySQL
- MySQL Connector for Python

---

## 📂 Project Structure

```
Password-Manager/
│
├── main.py                 # Main application
├── database.py             # Database connection
├── login.py                # Login module
├── add_password.py         # Add password functionality
├── view_password.py        # Display stored passwords
├── update_password.py      # Update credentials
├── delete_password.py      # Delete credentials
├── search.py               # Search functionality
├── config.py               # Database configuration
├── requirements.txt
├── screenshots/
│   ├── login.png
│   ├── dashboard.png
│   └── add_password.png
└── README.md
```

---

## 💾 Database Schema

### Database

```
password_manager
```

### Table: passwords

| Column | Data Type |
|----------|-----------|
| id | INT (Primary Key) |
| website | VARCHAR(100) |
| username | VARCHAR(100) |
| password | VARCHAR(255) |
| created_at | TIMESTAMP |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/password-manager.git
```

Navigate into the project directory

```bash
cd password-manager
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configure MySQL

Create a database

```sql
CREATE DATABASE password_manager;
```

Create the required table

```sql
CREATE TABLE passwords(
id INT AUTO_INCREMENT PRIMARY KEY,
website VARCHAR(100),
username VARCHAR(100),
password VARCHAR(255),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Update your database credentials inside:

```python
config.py
```

Example

```python
HOST = "localhost"
USER = "root"
PASSWORD = "your_password"
DATABASE = "password_manager"
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📸 Screenshots

Add screenshots inside the `screenshots` folder.

Example:

- Login Screen
- Dashboard
- Add Password
- View Passwords
- Search Password

---

## 🔒 Security

This project demonstrates password management functionality.

For production applications, consider:

- Password hashing using bcrypt
- AES encryption for stored passwords
- Environment variables for database credentials
- Multi-factor authentication
- Automatic backup
- Strong password generator

---

## 🚀 Future Enhancements

- Password Generator
- Password Strength Checker
- AES Encryption
- Export Passwords to CSV
- Import Passwords
- Cloud Backup
- Dark Mode
- Multi-user Authentication

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Python GUI development
- CRUD operations
- Database connectivity
- MySQL integration
- Object-Oriented Programming
- Event-driven programming
- Exception handling

---

## 👨‍💻 Author

**Priyanshu Sharma**

- Python Developer
- Data Analyst
- Machine Learning Enthusiast
