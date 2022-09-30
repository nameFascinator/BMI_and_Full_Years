"""GUI interface"""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    """UI MainWindow"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("background-color: rgb(255, 208, 131);")
        # MainWindow.setIconSize(QtCore.QSize(23, 24))
        # MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 382, 462))
        self.frame.setStyleSheet("background-color: rgb(255, 208, 131);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_Calculate = QtWidgets.QPushButton(self.frame)
        self.pushButton_Calculate.setGeometry(QtCore.QRect(300, 10, 71, 445))
        self.pushButton_Calculate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SizeAllCursor))
        self.pushButton_Calculate.setMouseTracking(True)
        self.pushButton_Calculate.setStyleSheet("background-color: rgb(255, 255, 0);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_Calculate.setObjectName("pushButton_Calculate")
        self.label_Years_Output = QtWidgets.QLabel(self.frame)
        self.label_Years_Output.setGeometry(QtCore.QRect(10, 412, 275, 41))
        self.label_Years_Output.setStyleSheet(
            "font: 75 18pt \"MS Shell Dlg 2\";\n""background-color: rgb(0, 0, 0);\n""color: rgb(85, 255, 127);")
        self.label_Years_Output.setObjectName("label_Years_Output")
        self.textEdit_Weight_Input = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Weight_Input.setGeometry(QtCore.QRect(80, 10, 204, 42))
        self.textEdit_Weight_Input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.textEdit_Weight_Input.setMouseTracking(True)
        self.textEdit_Weight_Input.setAccessibleName("")
        self.textEdit_Weight_Input.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n""font: 75 18pt \"MS Shell Dlg 2\";")
        self.textEdit_Weight_Input.setObjectName("textEdit_Weight_Input")
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setGeometry(QtCore.QRect(10, 200, 271, 51))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_Result = QtWidgets.QLabel(self.splitter_2)
        self.label_Result.setStyleSheet(
            "background-color: rgb(129, 129, 129);\n""color: rgb(255, 255, 255);\n""font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_Result.setObjectName("label_Result")
        self.label_Result_Output = QtWidgets.QLabel(self.splitter_2)
        self.label_Result_Output.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);\n""font: 18pt \"MS Shell Dlg 2\";")
        self.label_Result_Output.setObjectName("label_Result_Output")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(10, 120, 271, 41))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_BMI = QtWidgets.QLabel(self.splitter)
        self.label_BMI.setStyleSheet(
            "background-color: rgb(129, 129, 129);\n""color: rgb(255, 255, 255);\n""font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_BMI.setObjectName("label_BMI")
        self.lcdNumber_Output = QtWidgets.QLCDNumber(self.splitter)
        self.lcdNumber_Output.setStyleSheet("background-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 127);")
        self.lcdNumber_Output.setObjectName("lcdNumber_Output")
        self.label_Weight = QtWidgets.QLabel(self.frame)
        self.label_Weight.setEnabled(True)
        self.label_Weight.setGeometry(QtCore.QRect(11, 11, 59, 42))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Weight.setFont(font)
        self.label_Weight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Weight.setObjectName("label_Weight")
        self.label_Height = QtWidgets.QLabel(self.frame)
        self.label_Height.setGeometry(QtCore.QRect(11, 59, 59, 42))
        font = QtGui.QFont()
        font.setPointSize(14)
