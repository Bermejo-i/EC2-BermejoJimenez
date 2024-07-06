from PyQt5 import QtWidgets, uic
from Service import Service2
class Controller2:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/view2.ui")
        self.ventana.btn2.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()

    def onclickbtncalcular(self):
        resultado = 0
        
        try:
            num1 = int(self.ventana.punit.text())
            num2 = int(self.ventana.cant.text())
            resultado=Service2.total(num1,num2)
        finally:
            self.ventana.lblrespuesta.setText("El total de la venta es de: " + str(resultado) + " soles")