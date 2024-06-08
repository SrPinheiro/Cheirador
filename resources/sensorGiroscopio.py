from enums.direcao import Direcao
from pybricks.ev3devices import GyroSensor
from resources.defaultResource import Resource

class SensorGiroscopio(Resource):
    def __init__(self, port, positive_direction=Direcao.SENTIDOHORARIO):
        self.dispositivo = GyroSensor(port, positive_direction)
        self.porta = port

    def velocidade(self):
        return self.dispositivo.speed()

    def angulo(self):
        return self.dispositivo.angle()

    def resetar_angulo(self, angulo):
        self.dispositivo.reset_angle(angulo)
