'''En un estacionamiento cobran $/. 1.50 por hora o fracción. 
Determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, ingresando el tiempo en horas y minutos'''

from PyQt5 import QtWidgets, uic
from Service import Service1
class Controller1:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/1view.ui")
        self.ventana.btncalc.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()

    def onclickbtncalcular(self):
        resultado = 0
        
        try:
            num1 = int(self.ventana.hora.text())
            num2 = int(self.ventana.minuto.text())
            resultado=Service1.calcular(num1,num2)
        finally:
            self.ventana.lblresultado.setText("El monto total es de: " + str(resultado) + " soles")