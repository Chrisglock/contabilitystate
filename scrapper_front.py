
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt, QPoint
from PyQt5.QtGui import QMovie
from importlib.resources import path
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget
from scrapper_back import *


#"conseguir link post" 
   
#print(productos_listos)   
 
class Scrap(QWidget):    
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('scrapper_ventana.ui')
        self.ui.setWindowIcon(QtGui.QIcon('mono.png'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        #self.ui.setWindowFlags(Qt.FramelessWindowHint)
        
        #self.ui.show()
        self.ui.filtrar.clicked.connect(self.filtrar)
        
        self.e_carga()
        self.m_carga()
    

        
    def m_carga(self):
        self.ui.cargagif.setHidden(False)
    def e_carga(self):
        self.ui.cargagif.setHidden(True)
        
    def filtrar(self):
        
        if self.ui.lcuenta.text() !="" and self.ui.lproducto.text() !="":
            self.m_carga()
            productos_listos=search(self.ui.lcuenta.text(),self.ui.lproducto.text(),self.ui.ndatos.value())
            row=0
            self.ui.table.setRowCount(len(productos_listos))
            for i in productos_listos:
                self.ui.table.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))
                self.ui.table.setItem(row, 1, QtWidgets.QTableWidgetItem(i[2]))
                self.ui.table.setItem(row, 2, QtWidgets.QTableWidgetItem(i[3]))
                self.ui.table.setItem(row, 3, QtWidgets.QTableWidgetItem(i[1]))
                row=row+1
        
        else:
            QtWidgets.QMessageBox.about(self, 'Advertencia', 'Uno de los campos esta vacio!')
        #hacer subprocesos tal vez
        #WIDGET CARGA NO SE MUESTRA BIEN
        #ventana.e_carga()     
                
    def cerrar(self):
        self.movie.stop()
        self.close()
                     

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    scrap = Scrap()
    sys.exit(app.exec_())
