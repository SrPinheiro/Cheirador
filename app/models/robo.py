from app.models.cerebro import Cerebro
from app.models.motor import Motor
from app.configs.parametros import Parametros

class Robo:
    def __init__(self):
        self.cerebro = Cerebro()
        self.motorEsquerdo = Motor(Parametros.MOTORESQUERDO)
        self.motorDireito = Motor(Parametros.MOTORDIREITO)

    def andar(self):
        self.motorEsquerdo.acelerar(100)
        self.motorDireito.acelerar(100)
