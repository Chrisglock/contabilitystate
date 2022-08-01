from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt, QPointF 
from PyQt5.QtGui import QMovie , QPen
from importlib.resources import path
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget , QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis,QPieSeries , QLineSeries
import sys


class SegVentana(QWidget):    
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('segunda.ui')
        self.ui.setWindowIcon(QtGui.QIcon('mono.png'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        