from resources.sensorDeCor import SensorDeCor
from app.services.defaultService import Service
from configs.parametros import Parametros
import math

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

        colorVector.sort()

        centro = math.floor(Parametros.QUANT_AMOSTRAS_REFLEXAO / 2)

        correcao = Parametros.QUANT_AMOSTRAS_REFLEXAO % 2
        quantValores = math.floor(Parametros.QUANT_AMOSTRAS_REFLEXAO * Parametros.PORCENTAGEM_DE_AMOSTRAS_COR_VALIDAS) / 2
        inicio = math.floor(centro - quantValores)
        fim = math.ceil(centro + quantValores) + correcao

        media = 0

        for i in range(inicio, fim):
            media += colorVector[i]

        return media / (fim - inicio)


