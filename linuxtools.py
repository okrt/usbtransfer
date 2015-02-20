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

import dbus
import os

class PartitionUtils:
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.drives = {}
        self.devices = []

    def return_drives(self):
        return self.drives

    def add_device(self, dev, parent = None):
        mount = str(dev.GetProperty("volume.mount_point"))
        device = str(dev.GetProperty("block.device"))[:-1]

        self.drives[device] = {
            'label' : str(dev.GetProperty("volume.label")).replace(" ", "_"),
            'fstype' : str(dev.GetProperty("volume.fstype")),
            'fsversion': str(dev.GetProperty("volume.fsversion")),
            'uuid' : str(dev.GetProperty("volume.uuid")),
            'mount' : mount,
            'udi' : dev,
            'is_mount' : str(dev.GetProperty("volume.is_mounted")),
            'device' : device,
            'parent' : str(parent.GetProperty("block.device")),
            'size' : str(dev.GetProperty("volume.size"))
            }
    def add_dvd_device(self, dev, parent = None):
        mount = str(dev.GetProperty("volume.mount_point"))
        device = str(dev.GetProperty("block.device"))

        self.drives[device] = {
            'label' : str(dev.GetProperty("volume.label")).replace(" ", "_"),
            'fstype' : str(dev.GetProperty("volume.fstype")),
            'fsversion': str(dev.GetProperty("volume.fsversion")),
            'uuid' : str(dev.GetProperty("volume.uuid")),
            'mount' : mount,
            'udi' : dev,
            'is_mount' : str(dev.GetProperty("volume.is_mounted")),
            'device' : device,
            'parent' : str(parent.GetProperty("block.device")),
            'size' : str(dev.GetProperty("volume.size"))
            }
    def detect_removable_drives(self):
        hal_obj = self.bus.get_object("org.freedesktop.Hal",
                                 "/org/freedesktop/Hal/Manager")
        self.hal = dbus.Interface(hal_obj, "org.freedesktop.Hal.Manager")

        devices = self.hal.FindDeviceByCapability("storage")

        for device in devices:
            dev = self._get_device(device)

            if dev.GetProperty("storage.bus") == "usb":
                if dev.GetProperty("block.is_volume"):
                    self.add_device(dev)
                    continue

                else: 
                    children = self.hal.FindDeviceStringMatch("info.parent", device)

                    for child in children:
                        child = self._get_device(child)

                        if child.GetProperty("block.is_volume"):
                            self.add_device(child, parent = dev)

        if not len(self.drives):
            return False

        else:
            
            return True

    def detect_dvd_drives(self):
        hal_obj = self.bus.get_object("org.freedesktop.Hal",
                                 "/org/freedesktop/Hal/Manager")
        self.hal = dbus.Interface(hal_obj, "org.freedesktop.Hal.Manager")

        devices = self.hal.FindDeviceByCapability("storage.cdrom")

        for device in devices:
            dev = self._get_device(device)

            if dev.GetProperty("storage.bus") != "usb":
                try:
                    print str(dev.GetProperty("storage.bus"))
                except:
                    pass
                if dev.GetProperty("block.is_volume"):
                    self.add_dvd_device(dev)
                    continue

                else: 
                    children = self.hal.FindDeviceStringMatch("info.parent", device)

                    for child in children:
                        child = self._get_device(child)

                        if child.GetProperty("block.is_volume"):
                            self.add_dvd_device(child, parent = dev)

        if not len(self.drives):
            return False

        else:
            
            return True

    def mount_device(self, disk_dest):
        """ Mount our device with Hal if it is not already mounted"""
        device = self.drives[str(disk_dest)]
        mount_point = '/mnt/usbtransfer'

        device['udi'].Mount(mount_point, device['fstype'], dbus_interface = 'org.freedesktop.org.Hal.Device.Volume')

        device['is_mount'] = True
        device['mount'] = '/mnt/usbtransfer'
                
    def _get_device(self, udi):
        dev_obj = self.bus.get_object("org.freedesktop.Hal",udi)
        return dbus.Interface(dev_obj, "org.freedesktop.Hal.Device")


    def unmount_device(self, disk_dest):
      
        device = self.drives[disk_dest]
             
        device['udi'].Unmount([], dbus_interface='org.freedesktop.Hal.Device.Volume')
        device['is_mount'] = '0'
        device['mount'] = None
          
