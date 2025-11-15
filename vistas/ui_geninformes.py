# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geninformesnjtaOm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPushButton,
    QSizePolicy, QWidget, QMessageBox, QInputDialog, QFileDialog)
import os
from controladores import crearinforme

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(425, 336)
        Form.setMaximumSize(425, 336)
        Form.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"color:white;")
        self.btnGenInforme = QPushButton(Form)
        self.btnGenInforme.setObjectName(u"btnGenInforme")
        self.btnGenInforme.setGeometry(QRect(80, 140, 111, 23))
        self.btnGenInforme.setStyleSheet(u"background-color: blue;\n"
"color:white;\n"
"font: 700 9pt \"Segoe UI\";")
        self.comboBoxFicheros = QComboBox(Form)
        self.comboBoxFicheros.setObjectName(u"comboBoxFicheros")
        self.comboBoxFicheros.setGeometry(QRect(80, 170, 231, 23))
        self.comboBoxFicheros.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;")
        self.ruta_salida = QLineEdit(Form)
        self.ruta_salida.setObjectName(u"ruta_salida")
        self.ruta_salida.setGeometry(QRect(80, 280, 281, 23))
        self.ruta_salida.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;")
        self.ruta_salida.setReadOnly(True)
        self.ruta_entrada = QLineEdit(Form)
        self.ruta_entrada.setObjectName(u"ruta_entrada")
        self.ruta_entrada.setGeometry(QRect(80, 70, 281, 23))
        self.ruta_entrada.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;")
        self.ruta_entrada.setReadOnly(True)
        self.cdrTxtRutaEntrada = QPushButton(Form)
        self.cdrTxtRutaEntrada.setObjectName(u"cdrTxtRutaEntrada")
        self.cdrTxtRutaEntrada.setGeometry(QRect(80, 30, 111, 31))
        self.cdrTxtRutaEntrada.setStyleSheet(u"background-color: rgb(239, 159, 0);\n"
"color:white;\n"
"font: 700 9pt \"Segoe UI\";")
        self.cdrTxtRutaSalida = QPushButton(Form)
        self.cdrTxtRutaSalida.setObjectName(u"cdrTxtRutaSalida")
        self.cdrTxtRutaSalida.setGeometry(QRect(80, 240, 121, 31))
        self.cdrTxtRutaSalida.setStyleSheet(u"background-color: red;\n"
"color:white;\n"
"font: 700 9pt \"Segoe UI\";")

        self.retranslateUi(Form)
        
        
        self.cdrTxtRutaEntrada.clicked.connect(self.cambiar_ruta)
        self.cdrTxtRutaSalida.clicked.connect(self.cambiar_rutaPDF)
        self.btnGenInforme.clicked.connect(self.generar_informe)
        try:
            self.comboBoxFicheros.addItems(os.listdir(self.cdrTxtRutaEntrada.text()))
        except FileNotFoundError:
            self.aviso("Aviso ruta de entrada","Indica la ruta de los ficheros jrxml")



        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Generar Informes F\u00e1brica", None))
        self.btnGenInforme.setText(QCoreApplication.translate("Form", u"Generar Informe", None))
        self.ruta_salida.setText("")
        self.ruta_salida.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta ficheros generados", None))
#if QT_CONFIG(tooltip)
        self.ruta_entrada.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Pulsar enter para actualizar la lista de ficheros</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ruta_entrada.setText("")
        self.ruta_entrada.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta ficheros jrxml", None))
        self.cdrTxtRutaEntrada.setText(QCoreApplication.translate("Form", u"Ruta fichero jrxml", None))
        self.cdrTxtRutaSalida.setText(QCoreApplication.translate("Form", u"Ruta informes PDF", None))
    # retranslateUi

    def aviso(self,titulo,texto):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Aviso")
        dialogo.setText(texto)
        dialogo.exec()
    
    def pedir_parametros(self,pLista):
        #dialogo = QInputDialog.getText(self, pTitulo, pTexto)
        pTitulo = "Parámetros"
        pTexto = "Parámetros"
        sel, conf = QInputDialog.getItem(self, pTitulo, pTexto, pLista)
        if conf:
            if sel.isnumeric():
                return int(sel)
            else:
                return sel

    def error(self,pLista):
        return ""

    def generar_informe(self):
        
        # tupla control error si el fichero no está en eñ diccionario sql_param
        mens_error=("",self.error,"")
        """ 
        /home/luis/Dropbox/Instituto/VirtualShared/DI/EjemploTema7/informes
        asumo que si se han listado los ficheros, el directorio de entrada existe
            en cambio el de salida puede no existir, en ese caso aviso y genero en el directorio 
            de entrada
      """  
        """
        diccionario sel_param. Clave fichero a procesar.
        Dato tupla con el texto a mostrar
        al solicitar el parámetro (no lo estoy empleando. Mejora a futuro), método que solicita parámetro
        , en el caso que sea necesario, lista ara elegir 
        """
        sel_param={
    'Informe_Albaranes_PCliente':('ID__Cliente', self.pedir_parametros, ""),
    'Informe_Albaranes_PPedido':('ID__Pedido', self.pedir_parametros, ""),
    'Informe_AlbaranesSUB_PCliente':('ID__Cliente', self.pedir_parametros, ""),
    'Informe_AlbaranesSUB_PPedido':('ID__Pedido', self.pedir_parametros, ""),
    'Informe_SubEmpresaCliente':('ID__Cliente', self.pedir_parametros, ""), 
    'Informe_SubEmpresaPedido':('ID__Pedido', self.pedir_parametros, "")}  

    #InformePrincipal necesita indicar correctamente la ruta relativa de logo.png y de 
    #Subinformes....jasper
    # Modificar en JaspeSoft, en lugar de fichero o ./fichero debe ser informes/fichero
        
        ficheroEntrada = self.ruta_entrada.text()+"/"+self.comboBoxFicheros.currentText()
        #obtener el fichero seleccionado sin la extensión, para generar con .pdf
        ficheroSalida =  self.ruta_salida.text()+"/"+self.comboBoxFicheros.currentText()[:-6]
        if not os.path.exists(self.ruta_salida.text()): 
            ficheroSalida = ficheroEntrada[:-6]
            self.aviso("Atención","El directorio de salida "+self.ruta_salida.text()+" no existe\nInformes en directorio de entrada")

        
        
        #obtener el fichero seleccionado sin la extensión, para utilizarlo como clave en diccionario
        fichero_sel=self.comboBoxFicheros.currentText()[:-6]

        #Obtener parámetros en formato diccionario: {Nombre_parametro : parametro}
        #Con métodos get de diccionario, si no existe la clave, evitamos error, ejecutando método
        #error en tupla mens_error
        #elemento 0, es la clave del diccionario parametros o Nombre_parametro
        #elemento 1, es el parámetro, que se obtiene al ejecutar la función self.pedir_parametro
        #(el parámetro de la función self.pedir_parametro es el elemento 2)
        parametros={sel_param.get(fichero_sel,mens_error)[0]:
                    sel_param.get(fichero_sel,mens_error)[1]
                    (sel_param.get(fichero_sel,mens_error)[2])}

        crearinforme.advanced_example_using_database(ficheroEntrada,ficheroSalida,parametros)

        # Habrá que modificar pyreportjasper.py  para controlar el error si el fichero no tiene
        #formato adecuado    
   
    def cambiar_ruta(self):  
        self.ruta = QFileDialog.getExistingDirectory(self, "Seleccionar ruta en la que están los informes")
        self.ruta_entrada.setText(self.ruta)
        try:
            self.comboBoxFicheros.clear()
            items=os.listdir(self.ruta_entrada.text())
            #os.listdir(self.cdrTxtRutaEntrada.text()).sort()
            items.sort()
              
            self.comboBoxFicheros.addItems(items)
            
        except FileNotFoundError:
            self.aviso("Al cambiar ruta","No existe el directorio "+self.ruta_entrada.text())
            
    def cambiar_rutaPDF(self):
        self.ruta = QFileDialog.getExistingDirectory(self, "Seleccionar ruta en la que se generará el PDF del informe seleccionado")
        self.ruta_salida.setText(self.ruta)

import sys #Para que permita cerrar la ventana

class MiApp(QWidget,Ui_Form):
    # clase principal que crea nuestro interfaz
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       

   
if __name__ == "__main__":
    # Si no es utilizado como módulo, se jecutará
    #Simplemente abre la correspondiente ventana
    app = QApplication(sys.argv)
    mi_app = MiApp()
   
    mi_app.show()
    sys.exit(app.exec())