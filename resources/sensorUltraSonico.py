from pybricks.ev3devices import UltrasonicSensor
from resources.defaultResource import Resource

class SensorUltrassonico(Resource):
    def __init__(self, port):
        self.dispositivo = UltrasonicSensor(port)
        self.porta = port

    def distancia(self, silencioso=False):
        return self.dispositivo.distance(silent=silencioso)

    def presenca(self):
        return self.dispositivo.presence()