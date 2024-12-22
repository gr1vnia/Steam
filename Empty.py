from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

App = QApplication([])
Win = QWidget()
Win.resize(700, 500)
Win.setWindowTitle("Steam")
Win.show

LabelP = QLabel("")
W = QVBoxLayout()
W.addWidget(LabelP)


Win.setLayout
App.exec_()