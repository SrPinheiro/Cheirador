class BluetoothStatus:
    HOST = True
    CLIENT = False

class Bluetooth():
    CLIENT = BluetoothStatus.CLIENT
    HOST = BluetoothStatus.HOST

    def __init__(self, host):
        self.souHost = host