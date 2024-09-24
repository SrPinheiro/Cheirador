from FireWall.dispositivos.sensorGiroscopio import SensorGiroscopio
from FireWall.enums.porta import Porta
from FireWall.helpers.matematica import Matematica

class ServicoDeGiroscopio:
    def __init__(self, porta):
        self.giroscopio = SensorGiroscopio(porta)

    def getAngulo(self):
        amostras = []
        for _ in range(10):
            amostras.append(self.giroscopio.getAngulo()-10)
            
        tratamento = Matematica.MedianaPorVetor(amostras)
        return tratamento