from app.services.colorService import ColorService
from resources.cerebro import Cerebro
from configs.mapa import Mapa
from resources.motor import Motor
import math
class Sistema:
    def __init__(self):
        self.colorService = ColorService(Mapa.SENSORDIREITO)
        self.cerebro = Cerebro()
        motorL = Motor(Mapa.MOTORESQUERDO)
        motorR = Motor(Mapa.MOTORDIREITO)
        motorR.acelerar(10)
        motorL.acelerar(10)

   
    def run(self):
        menor = 99999999999999
        maior = 0

        while True:
            cor = self.colorService.getRGB()
            # if(cor > maior):
            #     maior = cor
            
            # if(cor < menor):
            #     menor = cor

            self.cerebro.limparTela()
            self.cerebro.escreverTexto(0, 0, cor)
            # self.cerebro.escreverTexto(0, 20, menor)
            # self.cerebro.escreverTexto(0, 40, maior)

