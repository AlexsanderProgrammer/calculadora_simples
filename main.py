from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import  QMessageBox


def somar_num():

        valor1 = tela.num1.text()
        valor2 = tela.num2.text()

        if valor1.isalpha() or valor2.isalpha():
            QMessageBox.about(tela,'Alerta', 'Digite apenas Numeros')

        res = int(valor1) + int(valor2)
        tela.visor.setText(str(res))
        tela.num1.setText('')
        tela.num2.setText('')

def diminuir_num():
    valor1 = tela.num1.text()
    valor2 = tela.num2.text()

    if valor1.isalpha() or valor2.isalpha():
        QMessageBox.about(tela,'Alerta', 'Digite apenas Numeros')

    res = int(valor1) - int(valor2)
    tela.visor.setText(str(res))
    tela.num1.setText('')
    tela.num2.setText('')

def dividir_num():
    valor1 = tela.num1.text()
    valor2 = tela.num2.text()

    if valor1.isalpha() or valor2.isalpha():
        QMessageBox.about(tela,'Alerta', 'Digite apenas Numeros')

    res = int(valor1) / int(valor2)
    tela.visor.setText(str(res))
    tela.num1.setText('')
    tela.num2.setText('')

def multiplicar_num():
    valor1 = tela.num1.text()
    valor2 = tela.num2.text()

    if valor1.isalpha() or valor2.isalpha():
        QMessageBox.about(tela,'Alerta', 'Digite apenas Numeros')

    res = int(valor1) * int(valor2)
    tela.visor.setText(str(res))
    tela.num1.setText('')
    tela.num2.setText('')

def apagar_visor():
    tela.visor.setText('0')

app = QtWidgets.QApplication([])
tela = uic.loadUi("calculadora_simples.ui")
tela.mais.clicked.connect(somar_num)
tela.menos.clicked.connect(diminuir_num)
tela.dividir.clicked.connect(dividir_num)
tela.multiplicar.clicked.connect(multiplicar_num)
tela.apagar.clicked.connect(apagar_visor)

tela.show()
app.exec()