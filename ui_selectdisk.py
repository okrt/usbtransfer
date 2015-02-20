# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectdisk.ui'
#
# Created: Sat Nov 12 05:54:02 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(287, 311)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Select your device", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/images/usbicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(True)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 342, 321))
        self.frame.setMinimumSize(QtCore.QSize(342, 321))
        self.frame.setMaximumSize(QtCore.QSize(342, 321))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/main/images/background.png);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(120, 280, 156, 23))
        self.buttonBox.setStyleSheet(_fromUtf8("background-image: url(:/main/images/trans.png);"))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.r_onlyremovable = QtGui.QRadioButton(self.frame)
        self.r_onlyremovable.setGeometry(QtCore.QRect(10, 220, 261, 16))
        self.r_onlyremovable.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.r_onlyremovable.setText(QtGui.QApplication.translate("Dialog", "Only Removable Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.r_onlyremovable.setChecked(True)
        self.r_onlyremovable.setObjectName(_fromUtf8("r_onlyremovable"))
        self.r_onlyusb = QtGui.QRadioButton(self.frame)
        self.r_onlyusb.setGeometry(QtCore.QRect(10, 240, 261, 16))
        self.r_onlyusb.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.r_onlyusb.setText(QtGui.QApplication.translate("Dialog", "Only USB Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.r_onlyusb.setObjectName(_fromUtf8("r_onlyusb"))
        self.r_alldevices = QtGui.QRadioButton(self.frame)
        self.r_alldevices.setGeometry(QtCore.QRect(10, 260, 261, 16))
        self.r_alldevices.setStyleSheet(_fromUtf8("background-image:url(:/main/images/trans.png);\n"
"color.rgb(0, 0, 0);"))
        self.r_alldevices.setText(QtGui.QApplication.translate("Dialog", "All Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.r_alldevices.setObjectName(_fromUtf8("r_alldevices"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 91, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/main/images/trans.png);"))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 231, 151))
        self.listWidget.setStyleSheet(_fromUtf8("background-image: url(:/main/images/white.png);"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.label.setStyleSheet(_fromUtf8("background-image: url(:/main/images/trans.png);"))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Select Your Device From List:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

