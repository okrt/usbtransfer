# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Nov 12 05:33:33 2011
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
        self.welcometext = QtGui.QLabel(self.frame)
        self.welcometext.setGeometry(QtCore.QRect(10, 10, 241, 41))
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
        self.versionLabel = QtGui.QLabel(self.frame)
        self.versionLabel.setGeometry(QtCore.QRect(110, 300, 221, 20))
        self.versionLabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"\n"
"color.rgb(0, 0, 0);"))
        self.versionLabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#0000ff;\">USBTransfer v3.0.1</span><span style=\" font-size:8pt;\"> - oguzkirat.com</span></p></body></html>")
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.transferlabel = QtGui.QLabel(self.frame)
        self.transferlabel.setGeometry(QtCore.QRect(10, 45, 231, 20))
        self.transferlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.transferlabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color: rgb(57, 57, 57);\n"
""))
        self.transferlabel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+QtGui.QApplication.translate("MainWindow", "Transfer distributions to USB drive", None, QtGui.QApplication.UnicodeUTF8)+"</span></p></body></html>")
        self.transferlabel.setObjectName(_fromUtf8("transferlabel"))
        self.Btn_cddvd = QtGui.QPushButton(self.frame)
        self.Btn_cddvd.setGeometry(QtCore.QRect(30, 134, 277, 44))
        self.Btn_cddvd.setMinimumSize(QtCore.QSize(277, 44))
        self.Btn_cddvd.setMaximumSize(QtCore.QSize(277, 44))
        self.Btn_cddvd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_cddvd.setToolTip(_fromUtf8(""))
        self.Btn_cddvd.setStyleSheet(_fromUtf8("border:none;\n"
"background-image: url(:/main/images/cddvd.png);\n"
""))
        self.Btn_cddvd.setText(QtGui.QApplication.translate("MainWindow", "CD or DVD", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_cddvd.setObjectName(_fromUtf8("Btn_cddvd"))
        self.Btn_isoimg = QtGui.QPushButton(self.frame)
        self.Btn_isoimg.setGeometry(QtCore.QRect(30, 85, 277, 44))
        self.Btn_isoimg.setMinimumSize(QtCore.QSize(277, 44))
        self.Btn_isoimg.setMaximumSize(QtCore.QSize(277, 44))
        self.Btn_isoimg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_isoimg.setToolTip(_fromUtf8(""))
        self.Btn_isoimg.setStyleSheet(_fromUtf8("border:none;\n"
"background-image: url(:/main/images/isoimg.png);\n"
""))
        self.Btn_isoimg.setText(QtGui.QApplication.translate("MainWindow", "ISO or IMG Image", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_isoimg.setObjectName(_fromUtf8("Btn_isoimg"))
        self.toolslabel = QtGui.QLabel(self.frame)
        self.toolslabel.setGeometry(QtCore.QRect(10, 179, 301, 16))
        self.toolslabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"\n"
"color.rgb(0, 0, 0);"))
        self.toolslabel.setText(QtGui.QApplication.translate("MainWindow", "Tools and Utilities", None, QtGui.QApplication.UnicodeUTF8))
        self.toolslabel.setObjectName(_fromUtf8("toolslabel"))
        self.Btn_download = QtGui.QPushButton(self.frame)
        self.Btn_download.setGeometry(QtCore.QRect(30, 198, 277, 44))
        self.Btn_download.setMinimumSize(QtCore.QSize(277, 44))
        self.Btn_download.setMaximumSize(QtCore.QSize(277, 44))
        self.Btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_download.setToolTip(_fromUtf8(""))
        self.Btn_download.setStyleSheet(_fromUtf8("border:none;\n"
"background-image: url(:/main/images/download.png);\n"
""))
        self.Btn_download.setText(QtGui.QApplication.translate("MainWindow", "Download a distribution", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_download.setObjectName(_fromUtf8("Btn_download"))
        self.Btn_format = QtGui.QPushButton(self.frame)
        self.Btn_format.setGeometry(QtCore.QRect(30, 248, 277, 44))
        self.Btn_format.setMinimumSize(QtCore.QSize(277, 44))
        self.Btn_format.setMaximumSize(QtCore.QSize(277, 44))
        self.Btn_format.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_format.setToolTip(_fromUtf8(""))
        self.Btn_format.setStyleSheet(_fromUtf8("border:none;\n"
"background-image: url(:/main/images/format.png);\n"
""))
        self.Btn_format.setText(QtGui.QApplication.translate("MainWindow", "Format drive", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_format.setObjectName(_fromUtf8("Btn_format"))
        self.wherelabel = QtGui.QLabel(self.frame)
        self.wherelabel.setGeometry(QtCore.QRect(10, 63, 321, 16))
        self.wherelabel.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.wherelabel.setText(QtGui.QApplication.translate("MainWindow", "Where do you want to transfer from?", None, QtGui.QApplication.UnicodeUTF8))
        self.wherelabel.setObjectName(_fromUtf8("wherelabel"))
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

