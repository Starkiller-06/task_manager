from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QMessageBox,
)

from finalProject import Task_manager
import mysql.connector
from PyQt5.QtGui import *
import sys
import bcrypt
from PyQt5.QtCore import *

db_conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="SQLRuiz06X!",
        database="tasks_py",
        auth_plugin="mysql_native_password")

if db_conn.is_connected():
    cursor = db_conn.cursor(buffered=True)

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Register")
        self.setGeometry(520, 200, 230, 100) 
        self.setStyleSheet("""
            background-color: #F8F8F8
        """)
        
        layout = QVBoxLayout()
        
        register_label = QLabel("CREATE ACCOUNT")
        register_label.setAlignment(Qt.AlignCenter)
        register_label.setStyleSheet(
        """
            color: #2D697A;
            font-weight: 1000;
            margin-top: 25px;
            margin-bottom: 25px
        """
        )
        register_label.setFont(QFont("Century Schoolbook", 11))
        layout.addWidget(register_label)
        

        self.new_user_name = QLineEdit()
        self.new_user_name.setMinimumHeight(30)
        new_user_label = QLabel("Create a user name:")
        new_user_label.setFont(QFont("Century Schoolbook", 11))
        layout.addWidget(new_user_label)
        layout.addWidget(self.new_user_name)
    
        
        self.new_email = QLineEdit()
        self.new_email.setMinimumHeight(30)
        new_email_label = QLabel("Enter your email:")
        new_email_label.setFont(QFont("Century Schoolbook", 11))
        layout.addWidget(new_email_label)
        layout.addWidget(self.new_email)

        self.new_password = QLineEdit()
        self.new_password.setMinimumHeight(30)
        new_passw_label = QLabel("Create a password:")
        new_passw_label.setFont(QFont("Century Schoolbook", 11))
        layout.addWidget(new_passw_label)
        layout.addWidget(self.new_password)
        
        self.create_account_btn = QPushButton("Create Account")
        layout.addWidget(self.create_account_btn)
        self.create_account_btn.setStyleSheet("""
            background-color: #CAE0E1;
            border-style: outset;
            border-width: 2px;      
            border-color: #2D697A;
            border-radius: 10px;    
            font: bold 11px;  
            padding: 3px                
        """)
        
        self.setLayout(layout)
        
    def confirm_msg(self):
        message = QMessageBox()
        message.setWindowTitle("Account Created")
        message.setText("Your account has been created. Welcome!")
        message.setIcon(QMessageBox.Information)
        m = message.exec_()
            

class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        
        self.registerWindow = None
        self.setWindowTitle("Log In")
        self.setStyleSheet("""
            background-color: #F8F8F8
        """)
        self.TaskManagerWindow = None
        
        layout = QVBoxLayout()
        
        welcome_label = QLabel("WELCOME TO YOUR TASK MANAGER!")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet(
        """
            color: #2D697A;
            font-weight: 1000;
            margin-top: 25px;
            margin-bottom: 25px
        """
        )
        welcome_label.setFont(QFont("Century Schoolbook", 11))
        layout.addWidget(welcome_label)

        self.user_name = QLineEdit()
        self.user_name.setMinimumHeight(30)
        user_name_label = QLabel("Enter user name or email:")
        user_name_label.setFont(QFont("Century Schoolbook", 11))
        layout.addWidget(user_name_label)
        layout.addWidget(self.user_name)

        self.password = QLineEdit()
        self.password.setMinimumHeight(30)
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Century Schoolbook", 11))
        layout.addWidget(password_label)
        layout.addWidget(self.password)
        
        self.logIn_btn = QPushButton("Log In")
        self.logIn_btn.setStyleSheet("""
            background-color: #CAE0E1;
            border-style: outset;
            border-width: 2px;      
            border-color: #2D697A;
            border-radius: 10px;    
            font: bold 11px;  
            padding: 3px                
        """)
        layout.addWidget(self.logIn_btn)
        
        not_acc = QLabel("If you don't have an account, register:")
        not_acc.setFont(QFont("Century Schoolbook", 9))
        not_acc.setAlignment(Qt.AlignCenter)
        not_acc.setStyleSheet(
        """
            color: gray;
            margin-top: 10px;
            margin-bottom: 10px
        """
        )
        layout.addWidget(not_acc)

        self.register_btn = QPushButton("Register")
        self.register_btn.setStyleSheet("""
            background-color: #CAE0E1;
            border-style: outset;
            border-width: 2px;      
            border-color: #2D697A;
            border-radius: 10px;    
            font: bold 11px;  
            padding: 3px          
        """)
        layout.addWidget(self.register_btn)
        
        self.register_btn.clicked.connect(self.show_new_window)
        self.logIn_btn.clicked.connect(self.log_into_account)
        self.setLayout(layout)
        
    def log_into_account(self):
        acc_identifier_inp = self.user_name.text() 
        password_inp = self.password.text()
        
        if acc_identifier_inp == "" or password_inp == "":
            
            self.message = QMessageBox()
            self.message.setWindowTitle("Error")
            self.message.setText("All fields are required. Try again.")
            self.message.setIcon(QMessageBox.Warning)
            m = self.message.exec_()

        else:
            query = f" SELECT User_Id, Account_name, Email, Password FROM users WHERE Account_name ='{acc_identifier_inp}' OR Email = '{acc_identifier_inp}'"
            cursor.execute(query)
            returned_row = cursor.fetchone() 
            
            if returned_row == None:
                self.message = QMessageBox()
                self.message.setWindowTitle("Invalid Credentials")
                self.message.setText("User not found")
                self.message.setIcon(QMessageBox.Warning)
                m = self.message.exec_()
                
            else:

                bd_hash_pw = returned_row[3].encode('utf-8') #This is the db hashted password
                hashing_pw_imp = password_inp.encode('utf-8') #This is the inputpassword
                
                result = bcrypt.checkpw(hashing_pw_imp, bd_hash_pw)
                
                if result == True:
                    user_id = returned_row[0]
                    user_name = returned_row[1]
                    self.TaskManagerWindow = Task_manager(user_id, user_name)
                    self.TaskManagerWindow.show()
                    self.close()
                    
                else:
                    self.message = QMessageBox()
                    self.message.setWindowTitle("Invalid Credentials")
                    self.message.setText("User or password incorrect")
                    self.message.setIcon(QMessageBox.Warning)
                    m = self.message.exec_()
        
    def show_new_window(self): 
        if(self.registerWindow is None):
            self.registerWindow = RegisterWindow()
            self.registerWindow.create_account_btn.clicked.connect(self.create_account)
            self.registerWindow.show()
            
    def hash_pw(self):
        acc_passw = self.registerWindow.new_password.text().encode('utf-8')
        salt = bcrypt.gensalt()
        hash_pw = bcrypt.hashpw(acc_passw, salt)
        
        return hash_pw
        
    def create_account(self):
        acc_name = self.registerWindow.new_user_name.text()
        acc_email = self.registerWindow.new_email.text()
        acc_passw = self.registerWindow.new_password.text()
        acc_hashed_pw = self.hash_pw().decode() #returns a string to save in db

        if acc_name == "" or acc_email == "" or acc_passw == "":
            self.message = QMessageBox()
            self.message.setWindowTitle("Error")
            self.message.setText("All fields are required")
            self.message.setIcon(QMessageBox.Warning)
            m = self.message.exec_()
        
        else: 
            query = f" SELECT User_Id, Account_name, Email, Password FROM users WHERE Account_name ='{acc_name}' OR Email = '{acc_email}'"
            cursor.execute(query)
            returned_row = cursor.fetchone() 
            
            if returned_row != None:
                self.message = QMessageBox()
                self.message.setWindowTitle("Account creation failed")
                self.message.setText("User or email already in use")
                self.message.setIcon(QMessageBox.Warning)
                m = self.message.exec_()
                
            else:
                query = f"INSERT INTO users (Account_name, Email, Password) VALUES ('{acc_name}', '{acc_email}', '{acc_hashed_pw}')"
                cursor.execute(query)
                db_conn.commit()
                
                self.registerWindow.confirm_msg()
                self.registerWindow.close()
                self.registerWindow = None
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogIn()
    window.show()
    sys.exit(app.exec_())
    