from datetime import date
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import *
from UI import Ui_MainWindow

# created by Viktor Chmilenko for his beloved wife Marina (Dr. Medizin)

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
                
    # created by Viktor Chmilenko for his beloved wife Marina (Dr. Medizin)
    
    def count_Age(self):
        now = date.today()
        year = self.ui.textEdit_Year_Input.toPlainText()
        month = self.ui.textEdit_Monthr_Input.toPlainText()
        day = self.ui.textEdit_Day_Input.toPlainText()

        if (len(year) or len(month) or len(day)) > 0:
            try:
                birthdate = date(int(year), int(month), int(day))
                age_in_years = (now - birthdate) / 365.2425
                age_in_years = str(age_in_years)
                age_in_years = age_in_years[:3]
                if int(age_in_years) < 150:
                    self.ui.label_Years_Output.setText(f"Full Years is:      {age_in_years}")
                else:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("???????????????????????????????????????")
                    dlg.setText(f"What!? you are {int(age_in_years)} years old!? I can not believe you!")
                    dlg.setIcon(QMessageBox.Icon.Question)
                    dlg.setStyleSheet("background-color: rgb(0, 255, 15);")
                    button = dlg.exec()
                    QMessageBox.StandardButton.Ok

            except:
                try:
                    if (len(year) or len(month) or len(day)) > 0 and (len(day) and len(month)) < 3 and (
                            (len(day) and len(month)) < 2 and int(month) < 12 and int(month) > 1 and int(
                            day) < 31 and int(day) > 1):
                        dlg = QMessageBox(self)
                        dlg.setWindowTitle("ERROR")
                        dlg.setText("Input should be integer or float number")
                        dlg.setIcon(QMessageBox.Icon.Warning)
                        dlg.setStyleSheet("background-color: rgb(180, 3, 3);")
                        button = dlg.exec()
                        QMessageBox.StandardButton.Ok
                    elif (len(day) or len(month)) > 2 or int(month) > 12 or int(month) < 1 or int(day) > 31 or int(
                            day) < 1:
                        dlg = QMessageBox(self)
                        dlg.setWindowTitle("ERROR")
                        dlg.setText("Month or Day incorrect")
                        dlg.setIcon(QMessageBox.Icon.Warning)
                        dlg.setStyleSheet("background-color: rgb(58, 169, 255);")
                        button = dlg.exec()
                        QMessageBox.StandardButton.Ok
                except:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("ERROR")
                    dlg.setText("Input should be integer or float number")
                    dlg.setIcon(QMessageBox.Icon.Warning)
                    dlg.setStyleSheet("background-color: rgb(180, 3, 3);")
                    button = dlg.exec()
                    QMessageBox.StandardButton.Ok
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = BMI_and_Full_Years()
    widget.setWindowIcon(QtGui.QIcon('.//files//smiley-fat.ico'))
    widget.show()
    app.exec()
    
    # created by Viktor Chmilenko for his beloved wife Marina (Dr. Medizin)
