
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt, QPointF 
from PyQt5.QtGui import QMovie , QPen
from importlib.resources import path
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget , QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis,QPieSeries , QLineSeries
from segunda import *
import sys
import pandas as pd
import openpyxl
excel_data = pd.read_excel('ventas.xlsx')
data = pd.DataFrame(excel_data, columns=['Producto', 'Stock', 'Vxsemana', 'Vxmes','Vxaño'])
print("The content of the file is:\n", data.iat[0,0])
class Ventana(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('grafic.ui')
        self.ui.setWindowIcon(QtGui.QIcon('mono.png'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.ui.der.clicked.connect(self.botonder)
        self.ui.izq.clicked.connect(self.botonizq)
        self.ui.boton.clicked.connect(self.abrirotra)
        self.ui.show()
        self.win = SegVentana()

        
        
        self.indice = 0
        
    def abrirotra(self):
        self.win.ui.show()
        
        
    def barras(self):
        #create barseries
        set0 = QBarSet("Parwiz")
        set1 = QBarSet("Karim")
        set2 = QBarSet("Tom")
        set3 = QBarSet("Logan")
        set4 = QBarSet("Bob")
 
 
        #insert data to the barseries
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2
 
        #we want to create percent bar series
        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
 
        #create chart and add the series in the chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Barchart Percent Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartThemeDark)
 
 
        #create axis for the chart
        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","asd"]
 
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
 
        #create chartview and add the chart in the chartview
        chartview = QChartView(chart)
 
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
 
        self.setLayout(vbox)

        self.ui.grafico1.setLayout(vbox)
        
    
    def torta(self):
        series  = QPieSeries()
        #append some data to the series 
        series.append("Apple", 80)
        series.append("Banana", 70)
        series.append("Pear", 50)
        series.append("Melon", 80)
        series.append("Water Melon", 30)
 
        #slice
        my_slice = series.slices()[3]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)
        my_slice.setPen(QPen(Qt.green, 4))
        my_slice.setBrush(Qt.green)
 
 
 
        #create QChart object
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Fruits Pie Chart")
        chart.setTheme(QChart.ChartThemeDark)
 
        # create QChartView object and add chart in thier 
        chartview = QChartView(chart)
 
 
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
 
        self.setLayout(vbox)
        self.ui.grafico2.setLayout(vbox)
    
    def puntos(self):
        series = QLineSeries()

        series.append(0,6)
        series.append(3,5)
        series.append(3,8)
        series.append(7,3)
        series.append(12,7)

        series << QPointF(11,1) << QPointF(13,3)\
        << QPointF(17,6) << QPointF(18,3) << QPointF(20,20)


        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Line Chart Example")
        chart.setTheme(QChart.ChartThemeBlueCerulean)


        chartview = QChartView(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
        self.setLayout(vbox)
        self.ui.grafico3.setLayout(vbox)
        
    def botonder(self):
        if self.indice < 2:
            self.indice+=1
            self.ui.stackedWidget.setCurrentIndex(self.indice)
            print(self.indice)
        else:
            print(self.indice)
            print("limite+")
        Ventana.plot(self)
 
    def botonizq(self):
        if self.indice > 0:
            self.indice-=1
            self.ui.stackedWidget.setCurrentIndex(self.indice)
            print(self.indice)
        else:
            print(self.indice)
            print("limite-")
        Ventana.plot(self)

    def plot(self):
        if self.indice == 0:
            Ventana.barras(self)
        elif self.indice == 1:
            Ventana.torta(self)
        elif self.indice == 2:
            Ventana.puntos(self)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())
