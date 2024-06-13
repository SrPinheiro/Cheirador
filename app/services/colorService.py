from resources.sensorDeCor import SensorDeCor
from app.services.defaultService import Service
from configs.parametros import Parametros
import math
from helpers.matematica import Matematica
class ColorService(Service):
    def __init__(self, porta):
        self.dispositivo = SensorDeCor(porta)

    def getCor(self):
        hashDeCores = { }
        moda = { "cor": None, "quant": 0 }

        for _ in range(Parametros.QUANT_AMOSTRAS_COR):
            corAtual = self.dispositivo.getCor()
            try:
                hashDeCores[corAtual] += 1
            except:
                hashDeCores[corAtual] = 1
                
            if hashDeCores[corAtual] > moda["quant"]:
                moda["cor"] = corAtual
                moda["quant"] = hashDeCores[corAtual]

        return moda["cor"]

    def getReflexao(self):
        colorVector = []

        for _ in range(Parametros.QUANT_AMOSTRAS_REFLEXAO):
            colorVector.append(self.dispositivo.reflexao())

        mediana = Matematica.MedianaPorVetor(colorVector)

        return mediana
    
    def getRGB(self):
        RED = []
        GREEN = []
        BLUE = []

        for _ in range(Parametros.QUANT_AMOSTRAS_RGB):
            RGB = self.dispositivo.getRGB()
            RED.append(RGB[0])
            GREEN.append(RGB[1])
            BLUE.append(RGB[2])

        MRED = Matematica.MedianaPorVetor(RED)
        MGREEN = Matematica.MedianaPorVetor(GREEN)
        MBLUE = Matematica.MedianaPorVetor(BLUE)

        return (MRED, MGREEN, MBLUE)
    
    def getColorAdvanced(self):
        pass

