import sys
'''
CREATE DATABASE password_mg;
USE password_mg;
CREATE TABLE password_table(
	Platform varchar(255) NOT NULL,
    Username varchar(255) NOT NULL,
    Passwrd varchar(255) NOT NULL,
    PRIMARY KEY (Platform)
);
'''

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from MainWindowUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)   

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())






    

                
