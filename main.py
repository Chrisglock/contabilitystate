
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt, QPoint
from PyQt5.QtGui import QMovie
from importlib.resources import path
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget
from scrapper_front import *
from InterfazComprobantes import *
from graficos import *
from funcionescyv import *
#"conseguir link post" 
   
#print(productos_listos)   
 
class Ventana(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('menu.ui')
        self.ui.setWindowIcon(QtGui.QIcon('mono.png'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        #self.ui.setWindowFlags(Qt.FramelessWindowHint)
        
        self.ui.show()
        self.scrap = Scrap()
        self.boleta = Boleta()
        self.grafico = Graficos()
        self.cyv = CYV()
        self.ui.comparador.clicked.connect(self.comp)
        self.ui.boletas.clicked.connect(self.boletas)
        self.ui.graficos.clicked.connect(self.graficos)
        self.ui.cv.clicked.connect(self.cyvv)
        #self.ui.filtrar.clicked.connect(self.filtrar)
    def comp(self):
        self.scrap.ui.show()
    def boletas(self):
        self.boleta.ui.show()
    def graficos(self):
        self.grafico.ui.show()
    def cyvv(self):
        self.cyv.ui.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())
