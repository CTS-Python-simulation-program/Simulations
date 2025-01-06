# CGP


from PyQt6 import QtCore, QtGui, QtWidgets
global runSim, trackArray
from sysFiles.plotting import Plot
import sysFiles.core as core
import datetime
import os
trackArray = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 502)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel {background-color: rgb(53, 53, 53);\n"
"font: 75 13pt \"Courier New\";\n"
"color: rgb(0, 230, 255);\n"
"padding: 7px;\n"
"border: 1px solid rgb(0, 230, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit{background-color: rgb(53, 53, 53);\n"
"font: 75 13pt \"Courier New\";\n"
"color: rgb(0, 230, 255);\n"
"padding: 7px;\n"
"border: 1px solid rgb(0, 230, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTextEdit {background-color:rgb(61, 61, 61); color: rgb(0, 230, 255);\n"
"font: 12px \"Courier New\";\n"
"border: 2px inset rgb(85,85,85);\n"
"border-radius: 10px;\n"
"padding: 7px;\n"
"}\n"
"\n"
"QPushButton { background-color: rgb(53, 53, 53);color: rgb(0, 230, 255);\n"
"border: 1px solid rgb(0, 230, 255);\n"
"border-radius: 10px;\n"
"padding: 7px;\n"
"font: 75 13pt \"Courier New\";\n"
"}\n"
"\n"
"QPushButton:hover {background-color: rgb(68, 68, 68); \n"
"border: 2px solid rgb(0, 255, 255); \n"
"}\n"
"\n"
"QPushButton:pressed {background-color: rgb(0, 230, 255); \n"
" color:rgb(0, 0, 0);\n"
"}\n"
"\n"
"QCheckBox {color:rgb(0, 230, 255);\n"
"font: 75 13pt \"Courier New\";;\n"
"padding: 7px;\n"
"}\n"
"\n"
"QCheckBox::indicator {width: 20px; height: 20px; \n"
"background-color: rgb(61, 61, 61);\n"
"border: 1px solid rgb(0, 230, 255);\n"
"border-radius: 7px;\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {background-color: rgb(0, 230, 255);\n"
"border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLCDNumber { background-color: rgb(44, 44, 44);\n"
"color:  rgb(0, 230, 255); \n"
"border: 2px solid rgb(0, 230, 255); \n"
"border-radius: 10px;\n"
"padding: 7px;\n"
"}\n"
"\n"
"\n"
"QWidget#circleWidget { background-color: rgb(92, 92, 92);\n"
"border: 3px solid rgb(0, 230, 255);\n"
"border-radius: 50%;\n"
"}\n"
"\n"
"QDial{ background-color: rgb(103, 103, 103);\n"
"border: 2px solid rgb(158, 158, 158);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 61, 191, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 191, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 161, 191, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 61, 104, 31))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 111, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 161, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.dial = QtWidgets.QDial(parent=self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(320, 41, 191, 171))
        self.dial.setStyleSheet("")
        self.dial.setMaximum(100000)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setObjectName("dial")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 131, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 60, 331, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 210, 331, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 160, 331, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(590, 400, 261, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        # self.checkBox_2.hide()
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 280, 841, 101))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(17)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 241, 31))
        self.label_5.setObjectName("label_5")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(360, 210, 111, 31))
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setDigitCount(6)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 841, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 110, 331, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(17, 400, 561, 23))
        self.progressBar.setStyleSheet("""
            QProgressBar {
                                text-align: right; /* Align the text to the left */
                            }

                            QProgressBar::chunk {
                                background: rgb(0, 230, 255);
                                border-radius: 0px;
                                width: 5px; /* Adjust the width of the chunks */
                            }

                            /* Windows 98 block-like design */
                            QProgressBar::chunk:horizontal {
                                border: 1px solid black;
                                border-radius: 0px;
                            }

                            QProgressBar::chunk:vertical {
                                border: 1px solid grey;
                                border-radius: 0px;
                            }

                            /* Set the block spacing */
                            QProgressBar::chunk:only-one {
                                border: 1px solid grey;
                                border-radius: 0px;
                            }

                            /* Add some text inside the chunks */
                            QProgressBar::chunk::text {
                                color: white;
                                font-size: 12px;
                            }
            """)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.dial.valueChanged.connect(self.update_lcd_number_2)
        self._update_timer = QtCore.QTimer()
        self.checkFirstRun = False
        self.pushButton_3.hide()
        self.pushButton_2.hide()
        self.pushButton_4.clicked.connect(lambda: self.getValuesAndRun(self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText(), self.dial.value()))
        self.pushButton_3.clicked.connect(self.showPlot)
        self.pushButton.clicked.connect(lambda: self.showPlotBeforeSim(self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText()))
        self.pushButton_2.clicked.connect(self.showPiArray)
        MainWindow.setStatusBar(self.statusbar)
        self._update_timer.timeout.connect(self.unhideIfFirstRunTrue)
        self._update_timer.start(100)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.checkCommandlineArgs()



    def checkCommandlineArgs(self):
        if len(sys.argv) == 5:
            # Set Values on display
            print("\n !! Commandline Override... !!")
            self.textEdit.setText(sys.argv[1])
            self.textEdit_2.setText(sys.argv[2])
            self.textEdit_3.setText(sys.argv[3])
            self.dial.setValue(int(sys.argv[4]))
            self.getValuesAndRun(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("No Commandline Args, skipping. Commandline Usage = python3 main.py <boxLen> <boxWidth> <radius> <iterations>")

    def unhideIfFirstRunTrue(self):
        if self.checkFirstRun == True:
            self.pushButton_3.show()
            self.pushButton_2.show()
        elif self.checkFirstRun == False:
            self.pushButton_3.hide()
            self.pushButton_2.hide()

    def update_lcd_number_2(self, value):
        self.lcdNumber_2.display(value)

    def showPlotBeforeSim(self, boxLen, boxWidth, radius):
        global runSim
        newPlot = Plot(
            float(boxLen),
            float(boxWidth),
            float(radius),
            [float(boxLen) / 2, float(boxWidth) / 2],
            [
                (float(boxLen) / 2) - ((float(boxLen) / 2) / 2),
                float(boxWidth) / 2,
            ],
            [
                (float(boxLen) / 2) + ((float(boxLen) / 2) / 2),
                float(boxWidth) / 2,
            ],
            [[0, 0]],
            "Before Simulation",
        )
        newPlot.plot_shapes()

    def showPlot(self):
        global runSim
        newPlot = Plot(
            runSim.boxLen,
            runSim.boxWidth,
            runSim.radius,
            runSim.boxCenterCoord,
            runSim.circleCenterCoord,
            runSim.squareCenterCoord,
            runSim.ballCoords,
            "After Simulation",
        )
        newPlot.plot_shapes()

    def saveArrayToMarkDown(self):
        global runSim, trackArray
        import csv
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"PiVariations/π_Array_iteration_{current_time}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["iterator", "pi Value"])
            for index, value in enumerate(runSim.π_Array):
                writer.writerow([index, value])

        trackArray += 1


    def showPiArray(self):
        global runSim
        newPlot = Plot(
            runSim.boxLen,
            runSim.boxWidth,
            runSim.radius,
            runSim.boxCenterCoord,
            runSim.circleCenterCoord,
            runSim.squareCenterCoord,
            runSim.ballCoords,
            "After Simulation",
        )
        newPlot.plot_π_Array(runSim.π_Array)
        self.saveArrayToMarkDown()


    def getValuesAndRun(self, boxLen, boxWidth, radius, iterations):
        global runSim
        self.checkFirstRun = False

        def update_progress(progress_value):
            self.progressBar.setValue(progress_value)
            self.dial.setValue(self.dial.value() - 1)

        runSim = core.Sim(
            float(boxLen), float(boxWidth), float(radius), int(iterations),
            progress_callback=update_progress
        )
        runSim.runSim()
        try:
            self.lcdNumber.setProperty("value", runSim.π_Array[-1])
            self.checkFirstRun = True
        except Exception as e:
            os.system(f"python3 sysFiles/anomaly.py '{e}, Set a proper iteration value !'")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CGP - Montecarlo | Task 1"))
        self.label.setText(_translate("MainWindow", "Box Length:"))
        self.label_2.setText(_translate("MainWindow", "Box Width:"))
        self.label_3.setText(_translate("MainWindow", "Circle Radius:"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Iterations</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Display plot before simulation"))
        self.pushButton_2.setText(_translate("MainWindow", "Pi Variation with time"))
        self.pushButton_3.setText(_translate("MainWindow", "Display plot after simulation"))
        self.checkBox_2.setText(_translate("MainWindow", "CUDA [Un-Available]"))
        self.label_5.setText(_translate("MainWindow", "Calculated Pi Value :"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Computing Group Project: Monte Carlo Simulation</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "▶ Run Simulation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
