# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'langselect.ui'
#
# Created: Sat Nov 12 05:33:11 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(340, 280)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(340, 280))
        MainWindow.setMaximumSize(QtCore.QSize(340, 280))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "USBTransfer", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/images/usbtransfer.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 342, 282))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/main/images/background.png);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.welcometext = QtGui.QLabel(self.frame)
        self.welcometext.setGeometry(QtCore.QRect(10, 10, 231, 41))
        self.welcometext.setStyleSheet(_fromUtf8("font: 30pt \"Myriad Pro\";\n"
"background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);"))
        self.welcometext.setText(QtGui.QApplication.translate("MainWindow", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.welcometext.setObjectName(_fromUtf8("welcometext"))
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(250, 0, 92, 92))
        self.widget.setMinimumSize(QtCore.QSize(92, 92))
        self.widget.setMaximumSize(QtCore.QSize(92, 92))
        self.widget.setToolTip(_fromUtf8(""))
        self.widget.setStyleSheet(_fromUtf8("background-image:url(:/main/images/usbicon.png);\n"
"border:none;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.selectlanguageLabel = QtGui.QLabel(self.frame)
        self.selectlanguageLabel.setGeometry(QtCore.QRect(10, 90, 321, 20))
        self.selectlanguageLabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);"))
        self.selectlanguageLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Please select your language:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.selectlanguageLabel.setObjectName(_fromUtf8("selectlanguageLabel"))
        self.langBox = QtGui.QComboBox(self.frame)
        self.langBox.setGeometry(QtCore.QRect(90, 120, 161, 21))
        self.langBox.setStyleSheet(_fromUtf8(""))
        self.langBox.setObjectName(_fromUtf8("langBox"))
        self.langBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.liste=['English']
        for x in sorted(os.listdir("lang")):
            if x.endswith(".qm"):
                self.liste.append(x[:-3])
        self.langBox.addItems(self.liste)
        self.translatenow = QtGui.QLabel(self.frame)
        self.translatenow.setGeometry(QtCore.QRect(10, 140, 321, 20))
        self.translatenow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.translatenow.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.translatenow.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; text-decoration: underline; color:#0000ff;\">Click here to translate  to your language.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.translatenow.setObjectName(_fromUtf8("translatenow"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 175, 44))
        self.pushButton.setMinimumSize(QtCore.QSize(175, 44))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/main/images/usbbutton.png);\n"
"border:none;"))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", ">> Continue", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.help = QtGui.QLabel(self.frame)
        self.help.setGeometry(QtCore.QRect(0, 210, 121, 16))
        self.help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.help.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Help</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.help.setObjectName(_fromUtf8("help"))
        self.checkupdatesBtn = QtGui.QLabel(self.frame)
        self.checkupdatesBtn.setGeometry(QtCore.QRect(0, 230, 121, 16))
        self.checkupdatesBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkupdatesBtn.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.checkupdatesBtn.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Check for updates</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkupdatesBtn.setObjectName(_fromUtf8("checkupdatesBtn"))
        self.aboutBtn = QtGui.QLabel(self.frame)
        self.aboutBtn.setGeometry(QtCore.QRect(0, 250, 121, 16))
        self.aboutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutBtn.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.aboutBtn.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">About</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutBtn.setObjectName(_fromUtf8("aboutBtn"))
        self.versionLabel = QtGui.QLabel(self.frame)
        self.versionLabel.setGeometry(QtCore.QRect(140, 260, 191, 20))
        self.versionLabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.versionLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#0000ff;\">USBTransfer v3.0.1</span><span style=\" font-size:8pt;\"> - oguzkirat.com</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.transferlabel = QtGui.QLabel(self.frame)
        self.transferlabel.setGeometry(QtCore.QRect(20, 50, 221, 20))
        self.transferlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.transferlabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.transferlabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Transfer distributions to USB drive</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.transferlabel.setObjectName(_fromUtf8("transferlabel"))
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

