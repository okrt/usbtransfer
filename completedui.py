# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'completed.ui'
#
# Created: Sat Nov 12 05:32:28 2011
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
        MainWindow.resize(340, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(340, 320))
        MainWindow.setMaximumSize(QtCore.QSize(340, 320))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "USBTransfer", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/images/usbtransfer.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 342, 321))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/main/images/background.png);\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.versionLabel = QtGui.QLabel(self.frame)
        self.versionLabel.setGeometry(QtCore.QRect(120, 300, 211, 20))
        self.versionLabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"background-repeat:no-repeat;\n"
"color.rgb(0, 0, 0);"))
        self.versionLabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#0000ff;\">USBTransfer v3.0.1</span><span style=\" font-size:8pt;\"> - oguzkirat.com</span></p></body></html>")
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.transferlabel = QtGui.QLabel(self.frame)
        self.transferlabel.setGeometry(QtCore.QRect(10, 40, 221, 20))
        self.transferlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.transferlabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.transferlabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Operation finished.", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.transferlabel.setObjectName(_fromUtf8("transferlabel"))
        self.selectisolabel = QtGui.QLabel(self.frame)
        self.selectisolabel.setGeometry(QtCore.QRect(10, 70, 321, 151))
        self.selectisolabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.selectisolabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "You\'ve successfully transferred your distribution to your device.", None,  QtGui.QApplication.UnicodeUTF8)+"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Now just boot your computer from USB drive and start installation or live CD/DVD.")+"</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br />"+QtGui.QApplication.translate("MainWindow", "Please check your distribution\'s web site for additional instructions about installing from USB.", None,  QtGui.QApplication.UnicodeUTF8)+"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "You should format your USB drive before using it.", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.selectisolabel.setWordWrap(True)
        self.selectisolabel.setObjectName(_fromUtf8("selectisolabel"))

        self.cdvdlabel = QtGui.QLabel(self.frame)
        self.cdvdlabel.setGeometry(QtCore.QRect(40, 4, 201, 41))
        self.cdvdlabel.setStyleSheet(_fromUtf8("font: 26pt \"Myriad Pro\";\n"
"background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);"))
        self.cdvdlabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Myriad Pro\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+QtGui.QApplication.translate("MainWindow", "Completed", None,  QtGui.QApplication.UnicodeUTF8)+"</p></body></html>")
        self.cdvdlabel.setObjectName(_fromUtf8("cdvdlabel"))
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

