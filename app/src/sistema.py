from configs.mapa import Mapa
from FireWall.servicos import ServicoDeCor
from FireWall.dispositivos import Motor

class Sistema:
    def __init__(self):
        self.RColorService = ServicoDeCor(Mapa.SENSORDIREITO)
        self.LColorService = ServicoDeCor(Mapa.SENSORESQUERDO)
        self.RMotor = Motor(Mapa.MOTORDIREITO)
        self.LMotor = Motor(Mapa.MOTORESQUERDO)
   
    def run(self):
        self.RMotor