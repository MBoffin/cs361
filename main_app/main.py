import zmq, sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from ui.main_window_ui import Ui_w_MainWindow

class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())