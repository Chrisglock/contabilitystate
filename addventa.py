from ast import Add
from audioop import add
import os
import pathlib
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt, QPoint
from PyQt5.QtGui import QMovie
from importlib.resources import path
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget, QDialog
from tkinter import Tk, Tcl
from tkinter.filedialog import askdirectory
from seleccionararchivo import *

class Addventa(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('addventa.ui')
        self.ui.setWindowIcon(QtGui.QIcon('mono.png'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        #self.ui.setWindowFlags(Qt.FramelessWindowHint)
        self.seleccionar = seleccionararchivo()
        self.ui.addventa.clicked.connect(self.addventa)

    def addventa(self):
        self.seleccionar.ui.show()