from resources.sensorDeCor import SensorDeCor
from app.services.defaultService import Service
from configs.parametros import Parametros
from helpers.matematica import Matematica
from enums.cor import Cor
class ColorService(Service):
    def __init__(self, porta):
        self.dispositivo = SensorDeCor(porta)
        self.GREEN = (7, 14, 13)
        self.BLACK = (5,5, 7)
        self.BLUE = (10, 11, 32)
        self.BROWN = (13, 6, 15)
        self.YELLOW = (59, 61, 38)
        self.WHITE =  (66, 80, 100)
        self.RED = (40, 7, 28)

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

        MRED = round(Matematica.MedianaPorVetor(RED))
        MGREEN = round(Matematica.MedianaPorVetor(GREEN))
        MBLUE = round(Matematica.MedianaPorVetor(BLUE))

        return (MRED, MGREEN, MBLUE)
    
    def getAdvancedColor(self):
        RGB = self.getRGB()

        diferencaPreto = Matematica.DiferencaPorVetor(RGB, self.BLACK)
        diferencaVerde = Matematica.DiferencaPorVetor(RGB, self.GREEN)
        diferencaAzul = Matematica.DiferencaPorVetor(RGB, self.BLUE)
        diferencaMarrom = Matematica.DiferencaPorVetor(RGB, self.BROWN)
        diferencaAmarelo = Matematica.DiferencaPorVetor(RGB, self.YELLOW)
        diferencaBranco = Matematica.DiferencaPorVetor(RGB, self.WHITE)
        diferencaVermelho = Matematica.DiferencaPorVetor(RGB, self.RED)

        menor = min(diferencaAzul, diferencaPreto, diferencaVerde, diferencaMarrom, diferencaAmarelo, diferencaBranco, diferencaVermelho)

        if(menor == diferencaPreto):
            return Cor.PRETO
        
        if(menor == diferencaVerde):
            return Cor.VERDE
        
        if(menor == diferencaAzul):
            return Cor.AZUL
        
        if(menor == diferencaMarrom):
            return Cor.MARROM
        
        if(menor == diferencaAmarelo):
            return Cor.AMARELO
        
        if(menor == diferencaBranco):
            return Cor.BRANCO
        
        if(menor == diferencaVermelho):
            return Cor.VERMELHO
        

    def getColorAdvanced(self):
        pass

