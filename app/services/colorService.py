from resources.sensorDeCor import SensorDeCor
from app.services.defaultService import Service
from configs.parametros import Parametros
from helpers.matematica import Matematica
from enums.cor import Cor
from enums.porta import Porta

class ColorService(Service):
    def __init__(self, porta, autoSalvarHistorico = True):
        # type: (Porta, bool) -> ColorService
        self.dispositivo = SensorDeCor(porta)
        self.autoSalvarHistorico = autoSalvarHistorico
        self.historicoCor = [None, None, None, None, None]
        self.historicoCorUnico = [None, None, None, None, None]
        self.historicoReflexao = [None, None, None, None, None]
        self.historicoRGB = [None, None, None, None, None]
        
        self.GREEN = (7, 14, 13)
        self.BLACK = (5,5, 7)
        self.BLUE = (10, 11, 32)
        self.BROWN = (13, 6, 15)
        self.YELLOW = (59, 61, 38)
        self.WHITE =  (66, 80, 100)
        self.RED = (40, 7, 28)
        
    def _autoSalvarHistorico(funcao):
        """
        * NÃO UTILIZE ESSA FUNCAO!
            Esta é uma funcao Wrapper que serve para salvar historico automaticamente e nao deve ser usada fora da classe
        """
        def funcaoWrapper(self):
            resultado = funcao(self)
            
            if(self.autoSalvarHistorico):
                self.adicionarCorNoHistorico(resultado)

            return resultado
        
        return funcaoWrapper

    @_autoSalvarHistorico
    def getCor(self):
        # type: () -> Cor
        """
        Faz o calculo da moda da cor que mais se repete, a quantidade de amostrar é definido pelo parametro QUANT_AMOSTRAS_COR
        
        :return Cor: Retorna o resultado da moda (objeto Cor)
        """
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
        # type: () -> int
        """
        Faz o calculo de uma media da mediana da reflexao, a quantidade de amostrar é definido pelo parametro QUANT_AMOSTRAS_REFLEXAO.
            A quantidade de amostras validas é definida pelo parametro: PORCENTAGEM_DE_AMOSTRAS_COR_VALIDAS
        
        :return int: Retorna o resultado da moda (objeto Cor)
        """
        colorVector = []

        for _ in range(Parametros.QUANT_AMOSTRAS_REFLEXAO):
            colorVector.append(self.dispositivo.getReflexao())

        mediana = Matematica.MedianaPorVetor(colorVector)

        return mediana

    def getRGB(self):
        # type: () -> tuple[int, int , int]
        """
        Faz o calculo de uma media da mediana das amostras de RGB, a quantidade de amostrar é definido pelo parametro QUANT_AMOSTRAS_RGB.
            A quantidade de amostras validas é definida pelo parametro: PORCENTAGEM_DE_AMOSTRAS_COR_VALIDAS
        
        :return tuple[int, int, int]: Retorna o resultado da media da mediana (objeto Cor)
        """
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

    @_autoSalvarHistorico
    def getColorAdvanced(self):
        # type: () -> Cor
        RGB = self.getRGB()
        
        cores = {
            Cor.PRETO: self.BLACK,
            Cor.VERDE: self.GREEN,
            Cor.AZUL: self.BLUE,
            Cor.MARROM: self.BROWN,
            Cor.AMARELO: self.YELLOW,
            Cor.BRANCO: self.WHITE,
            Cor.VERMELHO: self.RED
        }
        
        menor = float('inf')
        corMenor = None
        
        for cor, valor in cores.items():
            diferenca = Matematica.DiferencaPorVetor(RGB, valor)
            if diferenca < menor:
                menor = diferenca
                corMenor = cor
        
        return corMenor

    def adicionarCorNoHistorico(self, cor):
        #type: (Cor) -> None
        """
        Adiciona a cor no historico de cores
        """
        corDiferente = cor != self.historicoCorUnico[0]
        
        for i in range(4 , -1, -1):
            if i == 0:
                self.historicoCor[i] = cor
                if corDiferente:
                    self.historicoCorUnico[i] = cor
                break
            
            self.historicoCor[i] = self.historicoCor[i-1]
            if(corDiferente):
                self.historicoCorUnico[i] = self.historicoCorUnico[i-1]