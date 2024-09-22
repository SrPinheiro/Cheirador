from configs.mapa import Mapa
from FireWall.enums import Cor
from FireWall.dispositivos import Motor
from FireWall.services import ColorService

class Sistema:
    def __init__(self):
        self.RColorService = ColorService(Mapa.SENSORDIREITO)
        self.LColorService = ColorService(Mapa.SENSORESQUERDO)
        self.RMotor = Motor(Mapa.MOTORDIREITO)
        self.LMotor = Motor(Mapa.MOTORESQUERDO)
   
    def run(self):
        RColor = self.RColorService.getAdvancedColor()
        LColor = self.LColorService.getAdvancedColor()
        
        while True:
            if(not RColor == Cor.PRETO and not LColor == Cor.VERMELHO):
                self.LMotor.run(100)
            else:
                self.LMotor.stop()
            
            if(not LColor == Cor.PRETO and not RColor == Cor.VERMELHO):
                self.RMotor.run(100)
            else:
                self.RMotor.stop()