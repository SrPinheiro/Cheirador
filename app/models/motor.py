from pybricks.parameters import Direction, Stop
from pybricks.ev3devices import Motor as MotorLego

class Motor:
    def __init__(self, port, positive_direction=Direction.CLOCKWISE, gears=None):
        self.dispositivo = MotorLego(port, positive_direction, gears)
        #super().__init__(self.dispositivo)

    def getVelocidade(self):
        return self.dispositivo.speed()
    
    def getAngulo(self):
        return self.dispositivo.angle()
    
    def resetarAngulo(self, angulo):
        self.dispositivo.reset_angle(angulo)

    def soltarMotor(self):
        self.dispositivo.stop()
    
    def frearMotor(self):
        self.dispositivo.brake()

    def pararMotor(self):
        self.dispositivo.hold()

    def acelerar(self, velocidade):
        self.dispositivo.run(velocidade)
    
    def acelerarPorTempo(self, velocidade, tempo, entao=Stop.HOLD, esperar=True):
        self.dispositivo.run_time(velocidade, tempo, entao, esperar)

    def acelerarPorAngulo(self, velocidade, angulo, entao=Stop.HOLD, esperar=True):
        self.dispositivo.run_target(velocidade, angulo, entao, esperar)

    def acelerarAteParar(self, velocidade, entao=Stop.COAST, limite=None):
        self.dispositivo.run_until_stalled(velocidade,entao, limite)

    def rotacionar(self, taxa):
        self.dispositivo.dc(taxa)
