from PyQt5 import QtWidgets

import sys 

class MainWindow( QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("hello PyQt")
        l = QtWidgets.QLabel("My first PyQt app.")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()
    

if __name__ == '__main__':

        app = QtWidgets.QApplication(sys.argv)
        w = MainWindow()
        app.exec()