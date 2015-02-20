#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 Oğuz Kırat
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os, time, webbrowser, urllib, string, platform, shutil, tempfile
from PyQt4 import QtCore, QtGui
from mainui import Ui_MainWindow
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
import ui_selectdisk
import subprocess

osystem=sys.platform
scriptlocation=sys.path[0]
mbyte = (1024**2)
version=301

if osystem=="win32":
    from wintools import *
elif osystem=="linux2":
    from linuxtools import *
def ucwords( string ):
    erg=[ item.capitalize() for item in string.split( ' ' ) ]
    return ' '.join( erg )
def clickable(widget):

    class Filter(QtCore.QObject):
    
        clicked = QtCore.pyqtSignal()
        
        def eventFilter(self, obj, event):
        
            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    self.clicked.emit()
                    return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

class selectDisk(QtGui.QDialog, ui_selectdisk.Ui_Dialog):  
      def __init__(self):
	      QtGui.QDialog.__init__(self)
	      self.setupUi(self)
class CopyProgress(QtCore.QThread):
    procDone = QtCore.pyqtSignal(bool)
    partDone = QtCore.pyqtSignal(int)
    def run(self):
        if osystem=="win32":
            cmda = 'dd.exe if="'+sourceimg+'" of='+finaltarget+' bs=4M --progress' ##dd command
            print cmda
            wget_output = "" # Buffer to hold the result
            p = subprocess.Popen(str(cmda),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if p.stderr.read(75).count("Error")>0:
                try:
                    p.terminate()
                    p.kill()
                except:
                    pass
                wget_output = "" # reset
                cmda = 'dd.exe if="'+sourceimg+'" of=\\.\\\\'+finalvolumetarget+' bs=4M --progress'
                p = subprocess.Popen(str(cmda),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE) #Try again with volume name
            else:
                print "No error"
            while p.poll() is None:
                char = p.stderr.read(8)
                if char:
                    wget_output += char
                    mblist=wget_output.split('M \r')
                    if len(mblist)>3:
                        if mblist[-2].count(',')>=1:
                            completed=mblist[-2].replace(',','') #For values higher than 999 delete comma.
                        else:
                            completed=mblist[-2]
                        self.partDone.emit((int(completed)*100)/size)
                        time.sleep(0.13) #Just to keep it more responsive
            self.procDone.emit(True)
        elif osystem=="linux2":
            try:
                os.system("umount "+targetdisk)
                os.system("mkfs -t vfat "+targetdisk)
            except:
                pass
            amegabyte=(1024**2)
            completed=0
            sourceopened=open(sourceimg, 'r')
            targetopened=open(targetdisk, 'w')
            while completed<=size:
                data=sourceopened.read(amegabyte)
                targetopened.write(data)
                completed += 1
                self.partDone.emit(completed*100/size)
                time.sleep(0.13)
            self.procDone.emit(True)   

class Start(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.img_src=""
                self.disk_dest=""
        def warning_dialog(self, title, text):
                QtGui.QMessageBox.warning(self, title, text, QtGui.QMessageBox.Ok)
			
        def open_file(self):
                self.selected=QtGui.QFileDialog.getOpenFileName(self, self.tr("Select an ISO or IMG file"))
                if string.lower(unicode(self.selected)).endswith('.iso') or string.lower(unicode(self.selected)).endswith('.img'):
                    self.img_src=self.selected
                elif unicode(self.selected)=="":
                    self.warning_dialog(self.tr("Error!"), self.tr("You didn't selected a file."))
                    self.img_src=""
                else:
                    self.warning_dialog(self.tr("Error!"), self.tr("Selected file is not a ISO or IMG file"))
                    self.img_src=""
 

        def listdiskchange(self, checked=True):
            if checked:
                self.sd.listWidget.clear()
                if osystem=="win32":
                    self.driveliste={}
                    c = wmi.WMI()
                    if self.sd.r_alldevices.isChecked()==True:
                        for pm in c.Win32_DiskDrive():
                            self.driveliste[pm.index]=["Disk "+str(pm.index)+":"+str(pm.Model), pm.Model, pm.Name, pm.Partitions, pm.Size, pm.DeviceID, pm.index, pm.InterfaceType, pm.MediaType]
                        for a in self.driveliste:    
                            self.sd.listWidget.insertItem(0,self.driveliste[a][0])
                    if self.sd.r_onlyusb.isChecked()==True:
                        for pm in c.Win32_DiskDrive():
                            if pm.InterfaceType==u"USB":
                                self.driveliste[pm.index]=["Disk "+str(pm.index)+":"+str(pm.Model), pm.Model, pm.Name, pm.Partitions, pm.Size, pm.DeviceID, pm.index, pm.InterfaceType, pm.MediaType]
                        for a in self.driveliste:    
                            self.sd.listWidget.insertItem(0,self.driveliste[a][0])
                    if self.sd.r_onlyremovable.isChecked()==True:
                        for pm in c.Win32_DiskDrive():
                            if ucwords(str(pm.MediaType)).startswith("Removable Media"):
                                self.driveliste[pm.index]=["Disk "+str(pm.index)+":"+str(pm.Model), pm.Model, pm.Name, pm.Partitions, pm.Size, pm.DeviceID, pm.index, pm.InterfaceType, pm.MediaType]
                        for a in self.driveliste:    
                            self.sd.listWidget.insertItem(0,self.driveliste[a][0])
                else:
                    self.a = PartitionUtils()
                    self.a.detect_removable_drives()
                    for key in self.a.drives:
                        self.sd.listWidget.insertItem(0,key)
        def listdvdchange(self):
                self.sd.listWidget.clear()
                if osystem == "win32":
                    self.b = win32_PartitionUtils()
                    self.b.win32_detect_dvd_drives()
                for key in self.b.drives:
                        self.sd.listWidget.insertItem(0,key)
        def select_disk(self):
                self.temp_disk_dest=""
                self.disk_dest=""
                self.sd = selectDisk()
                if osystem == "win32":
                    self.listdiskchange(True)
                    self.connect(self.sd.r_onlyremovable, QtCore.SIGNAL("toggled(bool)"), self.listdiskchange)
                    self.connect(self.sd.r_alldevices, QtCore.SIGNAL("toggled(bool)"), self.listdiskchange)
                    self.connect(self.sd.r_onlyusb, QtCore.SIGNAL("toggled(bool)"), self.listdiskchange)
                elif osystem == 'linux2':
                    self.a = PartitionUtils()
                    self.a.detect_removable_drives()
                    for key in self.a.drives:
                        self.sd.listWidget.insertItem(0,key)
                    self.sd.r_onlyremovable.hide()
                    self.sd.r_onlyusb.hide()
                    self.sd.r_alldevices.hide()
                self.connect(self.sd.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.get_disk_destination)
                self.connect(self.sd.pushButton, QtCore.SIGNAL("clicked()"), self.listdiskchange)
                self.connect(self.sd.buttonBox, QtCore.SIGNAL("accepted()"), self.set_disk_destination)
                self.sd.exec_()
                QtCore.pyqtSignature("bool")
        def select_dvd(self):
                self.sd = selectDisk()
                if osystem == "win32":
                    self.b = win32_PartitionUtils()
                    self.b.win32_detect_dvd_drives()
                    for key in self.b.drives:
                        self.sd.listWidget.insertItem(0,key)
                elif osystem=="linux2":
                    self.b = PartitionUtils()
                    self.b.detect_dvd_drives()
                    for key in self.b.drives:
                        self.sd.listWidget.insertItem(0,key)
                self.sd.r_onlyremovable.hide()
                self.sd.r_onlyusb.hide()
                self.sd.r_alldevices.hide()
                self.connect(self.sd.pushButton, QtCore.SIGNAL("clicked()"), self.listdvdchange)	    	    
                self.connect(self.sd.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.get_dvd_destination)
                self.connect(self.sd.buttonBox, QtCore.SIGNAL("accepted()"), self.set_dvd_destination)
                self.sd.exec_()  
                QtCore.pyqtSignature("bool")


        def get_disk_destination(self, item):
                if item.text():
                    if osystem=='win32':
                        self.temp_disk_dest=str(item.text()).split(":")[0][5:]
                    else:
                        self.temp_disk_dest=str(item.text())
                    print self.temp_disk_dest
                else:
                    print "No text"
        def set_disk_destination(self):
            self.disk_dest=self.temp_disk_dest
        def get_dvd_destination(self, item):
                if item.text():
                    self.tmp_img_src = str(item.text())
                    print self.tmp_img_src
        def set_dvd_destination(self):
                self.img_src=self.tmp_img_src
                print self.img_src
        def updatePBar(self, val):
            self.ui.progressBar.setValue(val)   
            perct = "{0}%".format(val)
            self.ui.label.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">"+perct+'</span></p></body></html>')
            self.ui.label_2.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+self.tr("Transfered:")+str((val*size)/100)+" MB</span></p></body></html>")
            self.ui.label_3.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+self.tr("Total:") +str(size)+"  MB</span></p></body></html>")
            self.ui.label_4.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+self.tr("Remaining:")+str(size-((val*size)/100))+" MB</span></p></body></html>")
        def preparewin(self, targetdisk):
            if platform.win32_ver()[0]=="XP":
                c = wmi.WMI ()
                for physical_disk in c.Win32_DiskDrive ():
                    for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"):
                        for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"):
                            if int(physical_disk.Index)==int(self.disk_dest):
                                cmda="Echo E | format "+logical_disk.Caption+" /q /fs:FAT32"
                                os.popen(cmda)

            else:
                partitions=self.driveliste[int(targetdisk)][3]
                f=open("dps.txt", 'w')
                f.write("select disk "+str(targetdisk)+"\r\nclean\r\ncreate partition primary\r\nexit")
                f.close()
                os.popen("diskpart.exe /s dps.txt")
                os.remove("dps.txt")                
            p = subprocess.Popen('dd.exe --list',stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
            output, errors = p.communicate()
            b= errors.split("\r\n")
            for x in b:
                if x.count("\\\\?\\Device\\Harddisk"+targetdisk+"\\DR")>0:
                    global finaltarget
                    finaltarget=x.replace(" ", "").replace("linkto", "")
            c = wmi.WMI()
            for pm in c.Win32_PerfRawData_PerfDisk_PhysicalDisk():
                if pm.Name!=u"_Total":
                    a=pm.Name
                    b=a.split(" ")
                    if int(b[0])==int(self.disk_dest):
                        c=b[1]
                        global finalvolumetarget
                        finalvolumetarget="\\\\.\\"+c


        def fin(self):
            from completedui import Ui_MainWindow
            self.hide()
            QtGui.QWidget.__init__(self, None)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
            if unicode(self.selected)!=unicode(sourceimg):
                shutil.move(tempfile.gettempdir()+"\\temp.iso", unicode(self.selected))   
            try:
                isoname=unicode(self.selected).split("/")[-1].encode('ascii', 'ignore')
                webbrowser.open("http://www.oguzkirat.com/apps/usbtransfer/completed.php?ver="+str(version)+"&os="+urllib.pathname2url(isoname))
            except:
                pass

        def createfromimage(self):
            try:
                str(self.selected)
                self.img_src=self.selected
            except:
                self.onay=QtGui.QMessageBox.question(self, self.tr('Warning'),self.tr("Selected file's path is containing special characters. To prevent problems, USBTransfer will move it to temporary directory and move it back. Click Yes if you want to move the file to temporary directory or click No to cancel the operation and change the path yourself.\nWhile moving program may seem unresponsive."), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                if self.onay == QtGui.QMessageBox.Yes:
                    shutil.move(unicode(self.selected), tempfile.gettempdir()+"\\temp.iso")
                    self.img_src=tempfile.gettempdir()+"\\temp.iso"
                else:
                    self.img_src=""
            if unicode(self.img_src)!="" and self.disk_dest!="":
                self.img_size=os.stat(self.img_src).st_size
                if osystem=='win32':
                    self.disk_size = int(self.driveliste[int(self.disk_dest)][4])
                elif osystem=='linux2':
                    self.disk_size = (int(self.a.drives[self.disk_dest]['size']) * (1024*1024))
                global sourceimg
                sourceimg=self.img_src
                global targetdisk
                targetdisk=self.disk_dest
                global size
                size=self.img_size/(1024**2)
              
            
                if self.img_size > self.disk_size:
                    req_size = ((self.img_size - self.disk_size) / mbyte)
                    self.warning_dialog(self.tr("Error!"), self.tr("There is no enough space on the target disk!")+"\n"+str(req_size)+self.tr("MBs more needed."))
                else:
                    self.onay=QtGui.QMessageBox.question(self, self.tr('Warning'),self.tr("You will lose all the data in the disk. Do you want to continue?"), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if self.onay == QtGui.QMessageBox.Yes:
                        from progressui import Ui_MainWindow
                        self.hide()
                        QtGui.QWidget.__init__(self, None)
                        self.ui = Ui_MainWindow()
                        self.ui.setupUi(self)
                        self.show()
                        if osystem=="win32":
                            self.preparewin(targetdisk)
                        self.ui.thread = CopyProgress()
                        self.ui.thread.partDone.connect(self.updatePBar)
                        self.ui.thread.procDone.connect(self.fin)
                        self.ui.thread.start()

            
                    else:
                        self.warning_dialog(self.tr("Canceled"), self.tr("Transfer canceled!"))
            else:
                self.warning_dialog(self.tr("Cannot continue."), self.tr("ISO image or target disk wasn't selected!"))
                return True
        def createfromdvd(self):
            if self.img_src!="" and self.disk_dest!="":
                if osystem=='win32':
                    self.disk_size = int(self.driveliste[int(self.disk_dest)][4])
                    self.img_size = (int(self.b.drives[self.img_src]['size'])*(1024*1024))
                elif osystem=='linux2':
                    self.disk_size = (int(self.a.drives[self.disk_dest]['size']))
                    self.img_size = (int(self.b.drives[self.img_src]['size']))

                if osystem=="win32":
                    simg="\\\\.\\"+self.img_src
                else:
                    simg=self.img_src
                global sourceimg
                sourceimg=simg
                global targetdisk
                targetdisk=self.disk_dest
                global size
                size=self.img_size/(1024**2)
                if self.img_size > self.disk_size:
                    req_size = ((self.img_size - self.disk_size) / mbyte)
                    self.warning_dialog(self.tr("Error!"), self.tr("There is no enough space on the target disk!")+"\n"+str(req_size)+self.tr("MBs more needed."))
                else:
                    self.onay=QtGui.QMessageBox.question(self, self.tr('Warning'),self.tr("You will lose all the data in the disk. Do you want to continue?"), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if self.onay == QtGui.QMessageBox.Yes:
                        from progressui import Ui_MainWindow
                        self.hide()
                        QtGui.QWidget.__init__(self, None)
                        self.ui = Ui_MainWindow()
                        self.ui.setupUi(self)
                        self.show()
                        if osystem=="win32":
                            self.preparewin(targetdisk)
                        self.ui.thread = CopyProgress()
                        self.ui.thread.partDone.connect(self.updatePBar)
                        self.ui.thread.procDone.connect(self.fin)
                        self.ui.thread.start()
            
                    else:
                        self.warning_dialog(self.tr("Canceled!"), self.tr("Transfer canceled!"))
            else:
                self.warning_dialog(self.tr("Cannot continue."), self.tr("CD/DVD drive or target disk wasn't selected!"))
                return True
        @QtCore.pyqtSignature("bool")
        def formatting(self):
            if self.disk_dest!="":
                    self.onay=QtGui.QMessageBox.question(self, self.tr('Warning'),self.tr("You will lose all the data in the disk. Do you want to continue?"), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if self.onay == QtGui.QMessageBox.Yes:
                        if osystem=="win32":
                            os.popen(str('taskkill /f /im dd.exe')) 
                            if platform.win32_ver()[0]=="XP":
                                print "It is Windows XP"
                                self.preparewin(self.disk_dest)
                                cmda = 'dd.exe if=/dev/zero of='+finaltarget+' bs=512 count=1 --progress' ##dd command
                                print cmda
                                os.popen(cmda)
                                c = wmi.WMI ()
                                for physical_disk in c.Win32_DiskDrive ():
                                    for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"):
                                        for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"):
                                            if int(physical_disk.Index)==int(self.disk_dest):
                                                print logical_disk.Caption
                                                cmda="Echo E | format "+logical_disk.Caption+" /q /fs:FAT32"
                                                print cmda
                                                os.popen(cmda)
                                              

                            else:
                                f=open("dps.txt", 'w')
                                f.write("select disk "+str(self.disk_dest)+"\r\n")
                                f.write("clean\r\ncreate partition primary\n\rformat fs=FAT32 QUICK OVERRIDE\n\rexit")
                                f.close()
                                os.popen("diskpart.exe /s dps.txt")
                                os.remove("dps.txt")
                            self.warning_dialog(self.tr("Format Completed"), self.tr("Format completed, if it didn't work, try another format and partitioning tool to use your device."))

                        else:
                            f=open("dps.txt", 'w')
                            f.write("fdisk "+self.disk_dest+" << EOF\no\nn\np\n\n\n\nw\nEOF\numount "+self.disk_dest+"1\nmkfs -t vfat "+self.disk_dest+"1")
                            f.close()
                            os.system("chmod +x dps.txt")
                            os.system("./dps.txt")
                            self.warning_dialog(self.tr("Format Completed"), self.tr("You might need to restart your computer to use your device again."))
                        self.disk_dest=""


            else:
                self.warning_dialog(self.tr("Cannot continue."), self.tr("Target disk wasn't selected!"))                
        def backtomain(self):
            from mainui import Ui_MainWindow
            self.hide()
            QtGui.QWidget.__init__(self, None)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
            QtCore.QObject.connect(self.ui.Btn_cddvd, QtCore.SIGNAL("clicked()"), self.cddvd)
            QtCore.QObject.connect(self.ui.Btn_isoimg, QtCore.SIGNAL("clicked()"), self.isoimg)
            QtCore.QObject.connect(self.ui.Btn_format, QtCore.SIGNAL("clicked()"), self.formatpage)
            QtCore.QObject.connect(self.ui.Btn_download, QtCore.SIGNAL("clicked()"), self.downloaddist)
            self.selected=""
            self.img_src=""
            self.disk_dest=""
        def cddvd(self):
            self.disk_dest=""
            from cddvdui import Ui_MainWindow
            self.hide()
            QtGui.QWidget.__init__(self, None)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
            QtCore.QObject.connect(self.ui.Btn_Back, QtCore.SIGNAL("clicked()"), self.backtomain)
            QtCore.QObject.connect(self.ui.selectDVDButton, QtCore.SIGNAL("clicked()"), self.select_dvd)
            QtCore.QObject.connect(self.ui.selectUSBButton, QtCore.SIGNAL("clicked()"), self.select_disk)
            QtCore.QObject.connect(self.ui.Btn_cddvdStart, QtCore.SIGNAL("clicked()"), self.createfromdvd)
            QtCore.QObject.connect(self.ui.Btn_download, QtCore.SIGNAL("clicked()"), self.downloaddist)
        def isoimg(self):
            self.disk_dest=""
            from isoimgui import Ui_MainWindow
            self.hide()
            QtGui.QWidget.__init__(self, None)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
            QtCore.QObject.connect(self.ui.Btn_Back, QtCore.SIGNAL("clicked()"), self.backtomain)
            QtCore.QObject.connect(self.ui.Btn_download, QtCore.SIGNAL("clicked()"), self.downloaddist)
            QtCore.QObject.connect(self.ui.selectfileBtn, QtCore.SIGNAL("clicked()"), self.open_file)
            QtCore.QObject.connect(self.ui.selectUSBButton, QtCore.SIGNAL("clicked()"), self.select_disk)
            QtCore.QObject.connect(self.ui.Btn_cddvdStart, QtCore.SIGNAL("clicked()"), self.createfromimage)
        def formatpage(self):
            self.disk_dest=""
            from formatuiwin import Ui_MainWindow
            self.hide()
            QtGui.QWidget.__init__(self, None)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
            QtCore.QObject.connect(self.ui.selectUSBButton, QtCore.SIGNAL("clicked()"), self.select_disk)                
            QtCore.QObject.connect(self.ui.Btn_Back, QtCore.SIGNAL("clicked()"), self.backtomain)
            QtCore.QObject.connect(self.ui.Btn_formatStart, QtCore.SIGNAL("clicked()"), self.formatting)
        def webhelp(self):
            webbrowser.open("http://www.oguzkirat.com/usb-transfer-help")
        def translate(self):
            webbrowser.open("http://www.oguzkirat.com/usb-transfer-translations")
        def webupdate(self):
            try:
                con=urllib.urlopen("http://usbaktarici.googlecode.com/svn/trunk/version")
                data=con.read()
                con.close()
                if int(data)>301:
                        self.onay=QtGui.QMessageBox.question(self, _fromUtf8('Warning'),_fromUtf8("New version is available, do you want to download?"), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                        if self.onay == QtGui.QMessageBox.Yes:
                            webbrowser.open("http://www.oguzkirat.com/usb-transfer")
                else:
                    self.warning_dialog(self.tr("Warning"), self.tr("You are using the latest version."))
            except:
                self.warning_dialog(self.tr("Error"), self.tr("Couldn't connect to project web site."))
        def about(self):
            QtGui.QMessageBox.about(self, self.tr("About"), _fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p><strong>USBTransfer</strong><br />Version: 3.0.1</p><p>Developed and designed by:<br />Oğuz Kırat<br />http://www.oguzkirat.com</p><strong>Translations</strong><br /><strong>Arabic: </strong>Circoficus & zeugma<br /><strong>Dutch: </strong>Pjotr<br /><strong>Estonian: </strong>Rivo Zängov<br /><strong>German: </strong>Claas<br /><strong>Italian: </strong>Hüdaverdi Sarıaltın<br /><strong>Portuguese: </strong>Felipe Fzero<br /><strong>Russian: </strong>Alexey Ivanov<br /><strong>Spanish: </strong>Deicidium<p>©2011 Oğuz Kırat<br/>This program is distributed under the terms of the GNU General Public License as published by the Free Software Foundation.</body></html>"))

        def languageselector(self, parent=None):
            QtGui.QWidget.__init__(self, None)
            from langselectui import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
            QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.loadlanguage)
            clickable(self.ui.help).connect(self.webhelp)
            clickable(self.ui.checkupdatesBtn).connect(self.webupdate)
            clickable(self.ui.aboutBtn).connect(self.about)
            clickable(self.ui.translatenow).connect(self.translate)
            try:
                con=urllib.urlopen("http://usbaktarici.googlecode.com/svn/trunk/version")
                data=con.read()
                con.close()
                if int(data)>version:
                        self.onay=QtGui.QMessageBox.question(self, _fromUtf8('Warning'),_fromUtf8("New version is available, do you want to download?"), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                        if self.onay == QtGui.QMessageBox.Yes:
                            webbrowser.open("http://www.oguzkirat.com/usb-transfer")
            except:
                pass
        def downloaddist(self):
            webbrowser.open("http://www.oguzkirat.com/linux-distributions")

        def loadlanguage(self):
            self.selectedlanguage=self.ui.langBox.currentText()
            print self.selectedlanguage
            if self.selectedlanguage!="English":
                translator = QtCore.QTranslator(app)
                translator.load("lang/"+self.selectedlanguage+".qm")
                app.installTranslator(translator)
            if osystem=="win32":
                self.backtomain()
            else:
                self.backtomain()
if __name__ == "__main__":
    app= QtGui.QApplication(sys.argv)
    myapp = Start()
    myapp.languageselector()
    myapp.show()
    sys.exit(app.exec_())

