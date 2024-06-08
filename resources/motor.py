from pybricks.ev3devices import Motor as MotorLego
from enums.parada import Parada
from enums.direcao import Direcao
from resources.defaultResource import Resource

class Motor(Resource):
    def __init__(self, porta, positive_direction=Direcao.SENTIDOHORARIO, gears=None):
        self.dispositivo = MotorLego(porta, positive_direction, gears)
        self.porta = porta

    def getVelocidade(self):
        return self.dispositivo.speed()
    
    def getAngulo(self):
        return self.dispositivo.angle()
    
    def resetarAngulo(self, angulo):
        self.dispositivo.reset_angle(angulo)

    def soltarMotor(self):
        self.dispositivo.stop()
    
    def freioMotor(self):
        self.dispositivo.brake()

    def trancarMotor(self):
        self.dispositivo.hold()

    def acelerar(self, velocidade):
        self.dispositivo.run(velocidade)
    
    def acelerarPorTempo(self, velocidade, tempo, entao=Parada.PARAR, esperar=True):
        self.dispositivo.run_time(velocidade, tempo, entao, esperar)

    def acelerarPorAngulo(self, velocidade, angulo, entao=Parada.PARAR, esperar=True):
        self.dispositivo.run_target(velocidade, angulo, entao, esperar)

    def acelerarAteParar(self, velocidade, entao=Parada.PARAR, limite=None):
        self.dispositivo.run_until_stalled(velocidade,entao, limite)

    def rotacionar(self, taxa):
        self.dispositivo.dc(taxa)
