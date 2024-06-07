import pybricks.ev3devices as ev3

class SensorUltrassonico:
    def __init__(self, port):
        self.dispositivo = ev3.UltrasonicSensor(port)

    def distancia(self, silencioso=False):
        return self.dispositivo.distance(silent=silencioso)

    def presenca(self):
        return self.dispositivo.presence()
    