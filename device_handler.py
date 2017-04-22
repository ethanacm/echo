"""
holds devices needed for fauxmo server
"""
import device
import outlet_handler

class DeviceHandler:

    def __init__(self):
        self.outlet_handler = outlet_handler.OutletHandler()
        device_list = []
        device_list.append(device.Device(["goose berg", "honker"],  ))
        device_list.append((device.Device([])))





        self.device_list = []
        self.

