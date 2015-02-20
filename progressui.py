# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created: Sat Nov 12 08:07:50 2011
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "USBTransfer", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/images/usbtransfer.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.widget.setGeometry(QtCore.QRect(230, 0, 92, 92))
        self.widget.setMinimumSize(QtCore.QSize(92, 92))
        self.widget.setMaximumSize(QtCore.QSize(92, 92))
        self.widget.setToolTip(_fromUtf8(""))
        self.widget.setStyleSheet(_fromUtf8("background-image:url(:/main/images/usbicon.png);\n"
"border:none;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.welcometext = QtGui.QLabel(self.frame)
        self.welcometext.setGeometry(QtCore.QRect(10, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.welcometext.setFont(font)
        self.welcometext.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);"))
        self.welcometext.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Myriad Pro\'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">"+QtGui.QApplication.translate("MainWindow", "Transfering...", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.welcometext.setObjectName(_fromUtf8("welcometext"))
        self.transferlabel = QtGui.QLabel(self.frame)
        self.transferlabel.setGeometry(QtCore.QRect(10, 50, 211, 16))
        self.transferlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.transferlabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.transferlabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Please wait...", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.transferlabel.setObjectName(_fromUtf8("transferlabel"))
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 90, 301, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 120, 301, 20))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.label.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">"+QtGui.QApplication.translate("MainWindow", "Preparing...", None, QtGui.QApplication.UnicodeUTF8)+".</span></p></body></html>")
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 301, 20))
        self.label_2.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.label_2.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Transfered: ? MB", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 301, 20))
        self.label_3.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.label_3.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Total: ?  MB", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 301, 20))
        self.label_4.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.label_4.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Remaining: ? MB", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 301, 21))
        self.label_5.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.label_5.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Please do not interrupt the process...", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.label_5.setObjectName(_fromUtf8("label_5"))
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

