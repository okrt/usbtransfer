#!/usr/bin/python
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

import win32file, win32api
import os, wmi

class win32_PartitionUtils:
    def __init__(self):
        self.drives = {}
        
    def win32_get_total_size(drive=None):
        r = win32file.GetDiskFreeSpace('C:')
        capacity = r[3]*r[0]*r[1] / (1024**2)    #capacity = totalClusters*sectPerCluster*bytesPerSector as MegaByte
        return capacity

    def win32_detect_removable_drives(self):
        self.drives={}
        c = wmi.WMI()
        for pm in c.Win32_DiskDrive():
            self.drives[pm.index]=["Disk "+str(pm.index)+":"+str(pm.Model), pm.Model, pm.Name, pm.Partitions, str(pm.Size)[:-9], pm.DeviceID, pm.index, pm.InterfaceType, pm.MediaType]

    def win32_detect_dvd_drives(self):
        for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            try:
                drive = drive + ':'
                if win32file.GetDriveType(drive) == win32file.DRIVE_CDROM: #will be changed                    
                        r = win32file.GetDiskFreeSpace(drive)
                        capacity = r[3]*r[0]*r[1] / (1024**2)    #capacity = totalClusters*sectPerCluster*bytesPerSector as MegaByte
                        print capacity
                        print r
                        
                        self.drives[drive] = { 
                          'label': 'label', 
                          'mount': drive, 
                          'size': capacity,  
                          'device': drive,
                          'is_mount' : 1 # will be edited
                      } 
            except:
                pass
