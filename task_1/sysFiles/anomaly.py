from PyQt6.QtCore import QTimer, QMetaObject, Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainter
global x
x = 0
y = 0
autoClose = 0
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 204)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 0, 2, 255), stop:0.994924 rgba(0, 0, 0, 255));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 181))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 521, 41))
        self.label_2.setStyleSheet("background-color: rgb(54, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(200, 60, 331, 131))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(167, 0, 3);")
        self.textBrowser.setObjectName("textBrowser")

#####ANIMATE###########
        self._update_timer = QtCore.QTimer()
        self._update_timer.start(500)
        self._update_timer.timeout.connect(self.restartAnimation)
        self.update_error(sys.argv[1])
#######################


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def update_error(self,data):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Space Grotesk Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Error Details :</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[ERR_HANDLER]:"+data+"</p></body></html>"))

    def restartAnimation(self):
        global x,y, autoClose
        _translate = QtCore.QCoreApplication.translate
        if autoClose == 10:
            sys.exit()
        if x == 0:
            self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:78pt; font-weight:600; color:#9f0003;\">/ ! \\</span></p></body></html>"))
            self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ff0004;\">A N O M A L Y</span></p></body></html>"))
            x = 1
            y = 1
        else:
            self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:78pt; font-weight:600; color:#4a0001;\">/ ! \\</span></p></body></html>"))
            self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ff0004;\">A N O M A L Y</span></p></body></html>"))
            x = 0
        if y == 1:
            self.update_error(sys.argv[1])
            y = 0
        autoClose += 1
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Anomaly"))
        self.label.setPixmap(QtGui.QPixmap("ztos_stuff/zrn_logo_no_back.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("logo_zrn")
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:78pt; font-weight:600; color:#9f0003;\">/ ! \\</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Space Grotesk Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Error Details :</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[ERR_HANDLER]:LOADING DATA...</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
