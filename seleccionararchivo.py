from ast import Add
from audioop import add
from msilib.schema import CheckBox
import os
import pathlib
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt, QPoint
from PyQt5.QtGui import QMovie
from importlib.resources import path
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget, QDialog, QCheckBox
from tkinter import Tk, Tcl
from tkinter.filedialog import askdirectory

from numpy import void

class seleccionararchivo(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('seleccionararchivo.ui')
        self.ui.setWindowIcon(QtGui.QIcon('mono.png'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        #self.ui.setWindowFlags(Qt.FramelessWindowHint)
        #self.siguiente= next()
        #
        # self.ui.next.clicked.connect(self.next)

    def next(self):
        self.siguiente.ui.show()
        