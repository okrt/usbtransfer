# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format.ui'
#
# Created: Sat Nov 12 14:33:22 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(320, 240))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "USBTransfer", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/images/usbicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 322, 242))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(322, 242))
        self.frame.setMaximumSize(QtCore.QSize(322, 242))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/main/images/background.png);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(230, -8, 92, 92))
        self.widget.setMinimumSize(QtCore.QSize(92, 92))
        self.widget.setMaximumSize(QtCore.QSize(92, 92))
        self.widget.setToolTip(_fromUtf8(""))
        self.widget.setStyleSheet(_fromUtf8("background-image:url(:/main/images/usbicon.png);\n"
"border:none;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formatTitle = QtGui.QLabel(self.frame)
        self.formatTitle.setGeometry(QtCore.QRect(40, 4, 201, 41))
        self.formatTitle.setStyleSheet(_fromUtf8("font: 26pt \"Myriad Pro\";\n"
"background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);"))
        self.formatTitle.setText(QtGui.QApplication.translate("MainWindow", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.formatTitle.setObjectName(_fromUtf8("formatTitle"))
        self.formatLabel = QtGui.QLabel(self.frame)
        self.formatLabel.setGeometry(QtCore.QRect(26, 40, 191, 16))
        self.formatLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formatLabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.formatLabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Format drive", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.formatLabel.setObjectName(_fromUtf8("formatLabel"))
        self.Btn_formatStart = QtGui.QPushButton(self.frame)
        self.Btn_formatStart.setGeometry(QtCore.QRect(20, 190, 277, 44))
        self.Btn_formatStart.setMinimumSize(QtCore.QSize(277, 44))
        self.Btn_formatStart.setMaximumSize(QtCore.QSize(277, 44))
        self.Btn_formatStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_formatStart.setToolTip(_fromUtf8(""))
        self.Btn_formatStart.setStyleSheet(_fromUtf8("border:none;\n"
"background-image: url(:/main/images/cddvd.png);\n"
""))
        self.Btn_formatStart.setText(QtGui.QApplication.translate("MainWindow", "Start Formatting", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_formatStart.setObjectName(_fromUtf8("Btn_formatStart"))
        self.Btn_Back = QtGui.QPushButton(self.frame)
        self.Btn_Back.setGeometry(QtCore.QRect(1, 10, 30, 30))
        self.Btn_Back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_Back.setStyleSheet(_fromUtf8("background-image: url(:/main/images/back.png);\n"
"border:none;\n"
"\n"
""))
        self.Btn_Back.setText(_fromUtf8(""))
        self.Btn_Back.setObjectName(_fromUtf8("Btn_Back"))
        self.descLabel = QtGui.QLabel(self.frame)
        self.descLabel.setGeometry(QtCore.QRect(10, 110, 301, 51))
        self.descLabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.descLabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "If you cannot use your device after transfer you can format it.", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.descLabel.setWordWrap(True)
        self.descLabel.setObjectName(_fromUtf8("descLabel"))
        self.selectandstartLabel = QtGui.QLabel(self.frame)
        self.selectandstartLabel.setGeometry(QtCore.QRect(10, 160, 301, 21))
        self.selectandstartLabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.selectandstartLabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Select your device and click &quot;Start Formatting&quot;.", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.selectandstartLabel.setObjectName(_fromUtf8("selectandstartLabel"))
        self.selectUSBButton = QtGui.QPushButton(self.frame)
        self.selectUSBButton.setGeometry(QtCore.QRect(80, 70, 175, 44))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(7)
        self.selectUSBButton.setFont(font)
        self.selectUSBButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectUSBButton.setStyleSheet(_fromUtf8("border:none;\n"
"background-image: url(:/main/images/usbbutton.png)\n"
""))
        self.selectUSBButton.setText(QtGui.QApplication.translate("MainWindow", "Select USB Drive", None, QtGui.QApplication.UnicodeUTF8))
        self.selectUSBButton.setObjectName(_fromUtf8("selectUSBButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

