import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from login_form_ui import Ui_Dialog
from query.selects import select_login_, select_email_, post_user
from set import email_admin, email_doctor
class Reg_window(QtWidgets.QDialog, Ui_Dialog):
    def init(self):
        super().init()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.register)

    @staticmethod
    def create_user(login, password, email):
        role_id = 5
        if email in email_admin:
            role_id = 1
        elif email in email_doctor:
            role_id = 2
        post_user(login, password, email, role_id)

    def register(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        if login and password and email:
            existing_user = select_login_(login)
            existing_email = select_email_(email)
            if not existing_user and not existing_email:
                create = self.create_user(login, password, email)
                if create:
                    print("Пользователь создан")
            else:
                if existing_user:
                    "Пользователь с логином существует"
                if existing_email:
                    "Пользователь с эмейл существует"
        else:
            print("Введите логин и пароль")


app = QApplication(sys.argv)
dialog = Reg_window()
dialog.show()
sys.exit(app.exec_())