from resources.defaultResource import Resource
from pybricks.ev3devices import InfraredSensor

class SensorInfravermelho(Resource):
    def __init__(self, port):
        self.dispositivo = InfraredSensor(port)
        self.porta = port

    def distancia(self):
        return self.dispositivo.distance()

    def distancia_controle(self, canal):
        return self.dispositivo.beacon(canal)

    def getBotoes(self, canal):
        return self.dispositivo.buttons(canal)

    def teclado(self):
        return self.dispositivo.keypad()
