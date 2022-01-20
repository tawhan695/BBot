
from server import API

import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        # st = self.Login()
        # print('api',st[0])  
        # if st[0]:
        #     self.Init(MainWindow)
            
        #test
        self.Init(MainWindow)

    
    def Login(self):
        api = API().Login()
          
        return api
        
    def Init(self,QWindow):
        QWindow.setWindowTitle("BeBot Dashbord")
        QWindow.setAutoFillBackground(True)
        QWindow.setWindowOpacity(0.9)
        QWindow.setWindowModality(QtCore.Qt.ApplicationModal)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
   
    