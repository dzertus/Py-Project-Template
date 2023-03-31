# Template file
"""
View Classes
"""
from PySide2 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """

        """
        super(InterfaceAbstract).__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.set_central_widget()
