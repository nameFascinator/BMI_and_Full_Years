from datetime import date
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import *
from UI import Ui_MainWindow


class BMI_and_Full_Years(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BMI and Full Years")

        self.ui.pushButton_Calculate.pressed.connect(self.count_BMI)
        self.ui.pushButton_Calculate.pressed.connect(self.count_Age)

    def count_BMI(self):
        weight = self.ui.textEdit_Weight_Input.toPlainText()
        height = self.ui.textEdit_Height_Input.toPlainText()

        try:
            BMI = round(float(weight) / (float(height) / 100 * float(height) / 100), 2)
            self.ui.lcdNumber_Output.display(BMI)

            if int(BMI) < 18.5:
                self.ui.label_Result_Output.setText(" underweight")
                self.ui.label_Result_Output.setStyleSheet(
                    "background-color: rgb(0, 0, 0);\n""color: rgb(70, 133, 153);\n""font: 18pt \"MS Shell Dlg 2\";")

            elif int(BMI) < 25:
                self.ui.label_Result_Output.setText(" normal weight")
                self.ui.label_Result_Output.setStyleSheet(
                    "background-color: rgb(0, 0, 0);\n""color: rgb(79, 198, 183);\n""font: 18pt \"MS Shell Dlg 2\";")

            elif int(BMI) < 30:
                self.ui.label_Result_Output.setText(" slightly overweight")
                self.ui.label_Result_Output.setStyleSheet(
                    "background-color: rgb(0, 0, 0);\n""color: rgb(240, 201, 33);\n""font: 16pt \"MS Shell Dlg 2\";")

            elif int(BMI) < 35:
                self.ui.label_Result_Output.setText(" obese")
                self.ui.label_Result_Output.setStyleSheet(
                    "background-color: rgb(0, 0, 0);\n""color: rgb(237, 158, 147);\n""font: 18pt \"MS Shell Dlg 2\";")

            else:
                self.ui.label_Result_Output.setText(" clinically obese")
                self.ui.label_Result_Output.setStyleSheet(
                    "background-color: rgb(0, 0, 0);\n""color: rgb(203, 73, 72);\n""font: 18pt \"MS Shell Dlg 2\";")

        except:
            if (len(weight) or len(height)) > 0:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("ERROR")
                dlg.setText("Input should be integer or float number")
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.setStyleSheet("background-color: rgb(180, 3, 3);")
                button = dlg.exec()
                QMessageBox.StandardButton.Ok
