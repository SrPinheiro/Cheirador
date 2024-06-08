from resources.cerebro import Cerebro
from resources.motor import Motor
from configs.mapa import Mapa
from app.models.defaultModel import Model
from configs.parametros import Parametros

class Robo(Model):
    def __init__(self):
        self.cerebro = Cerebro()
        self.motorEsquerdo = Motor(Mapa.MOTORESQUERDO)
        self.motorDireito = Motor(Mapa.MOTORDIREITO)

        self.cerebro.imprimirImagem(Parametros.LOGO)

    def andar(self):
        self.motorEsquerdo.acelerar(100)
        self.motorDireito.acelerar(100)
