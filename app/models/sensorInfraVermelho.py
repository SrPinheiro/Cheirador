import pybricks.ev3devices as ev3

class SensorInfravermelho:
    def __init__(self, port):
        self.dispositivo = ev3.InfraredSensor(port)

    def distancia(self):
        return self.dispositivo.distance()

    def distancia_controle(self, canal):
        return self.dispositivo.beacon(canal)

    def getBotoes(self, canal):
        return self.dispositivo.buttons(canal)

    def teclado(self):
        return self.dispositivo.keypad()
