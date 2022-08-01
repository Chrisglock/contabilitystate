import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtGui import QImage
import cv2
import numpy as np
import copy

class Boleta(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('InterfazComprobantes.ui')
        #self.ui.show()
        #self.ui.agregarfoto.setStyleSheet("background-image : url(62319.png);")
        self.ui.agregarfoto.clicked.connect(self.Abrir2) 
        self.ui.actionCerrar.triggered.connect(self.Cerrar)
        self.ui.actionFoto.triggered.connect(self.Abrir) 
        
    def Abrir(self):
        path,_= QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir archivo', '.')
        self.img = cv2.imread(path)
        self.img = cv2.resize(self.img, (400,400))
        self.setPhoto(self.img)
    
    def setPhoto(self, img):
        self.tmp = img
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.ui.visor.setPixmap(QtGui.QPixmap.fromImage(img))
        
    def Abrir2(self):
        path2,_= QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir archivo', '.')
        self.img2 = cv2.imread(path2)
        self.img2 = cv2.resize(self.img2, (400,400))
        self.setPhoto2(self.img2)        

    def setPhoto2(self, img2):
        self.tmp2 = img2
        frame2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img2 = QImage(frame2, frame2.shape[1], frame2.shape[0], frame2.strides[0], QImage.Format_RGB888)
        self.ui.visor_2.setPixmap(QtGui.QPixmap.fromImage(img2))
        
    def Cerrar(self):
        self.ui.close()

#app = QtWidgets.QApplication(sys.argv)
#ventana = Boleta()
#sys.exit(app.exec())