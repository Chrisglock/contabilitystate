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
from añadir import *
from addventa import *

class VentanaCYV(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('gestioncyv.ui')
        self.ui.setWindowIcon(QtGui.QIcon('mono.png'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        #self.ui.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.show()
        self.añadir = VentanaAdd()
        self.ui.exam.clicked.connect(self.exam)
        self.ui.add.clicked.connect(self.add)

    def exam(self):
        Tk().withdraw()
        filename=askdirectory(
            initialdir="C://"
        )
        #path=pathlib.Path(filename).absolute()
        archivos = os.listdir(path)
        path,_= QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir archivo', '.')
        archivos = list(
            filter(
                lambda name: ".xscl" or ".xlsx" in name,
                archivos
            )
        )
    def add(self):
        self.añadir.ui.show()

    def cerrar(self):
        self.movie.stop()
        self.close

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaCYV()
    sys.exit(app.exec_())