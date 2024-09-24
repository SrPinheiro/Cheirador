from FireWall.enums.cor import Cor
from FireWall.enums.porta import Porta
from FireWall.helpers.matematica import Matematica
from FireWall.servicos.servicoDefault import ServicoDefault
from FireWall.dispositivos.sensorDeCor import SensorDeCor
from FireWall.configs.parametros import Parametros
from FireWall.helpers.wrappers import autoSalvarHistoricoDeCor

class ServicoDeCor(ServicoDefault):
    """
    Classe responsável pelo serviço de detecção de cores, possui diversas funcoes que ajudam a utilizar o sensor.
    """

    def __init__(self, porta, autoSalvarHistorico=True):
        # type: (Porta, bool) -> ServicoDeCor
        """
        Inicializa uma instância do ColorService.

        :param porta: Porta na qual o sensor de cor está conectado.
        :param autoSalvarHistorico: Indica se o histórico de cores deve ser salvo automaticamente.
        """
        self.dispositivo = SensorDeCor(porta)
        self._autoSalvarHistorico = autoSalvarHistorico
        self._historicoCor = [Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE]
        self._historicoCorUnico = [Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE]
        
        self.GREEN = (7, 14, 13)
        self.BLACK = (5, 5, 7)
        self.BLUE = (10, 11, 32)
        self.BROWN = (13, 6, 15)
        self.YELLOW = (59, 61, 38)
        self.WHITE = (66, 80, 100)
        self.RED = (40, 7, 28)

    @autoSalvarHistoricoDeCor
    def getCor(self):
        # type: () -> Cor
        """
        Calcula a moda da cor que mais se repete.

        A quantidade de amostras é definida pelo parâmetro QUANT_AMOSTRAS_COR.

        :return: Cor que mais se repete (objeto Cor).
        """
        hashDeCores = {}
        moda = {"cor": None, "quant": 0}

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
        Calcula a mediana da reflexão.

        A quantidade de amostras é definida pelo parâmetro QUANT_AMOSTRAS_REFLEXAO.
        A quantidade de amostras válidas é definida pelo parâmetro PORCENTAGEM_DE_AMOSTRAS_COR_VALIDAS.

        :return: Mediana da reflexão (int).
        """
        colorVector = []

        for _ in range(Parametros.QUANT_AMOSTRAS_REFLEXAO):
            colorVector.append(self.dispositivo.getReflexao())

        mediana = Matematica.MedianaPorVetor(colorVector)

        return mediana

    def getRGB(self):
        # type: () -> tuple[int, int, int]
        """
        Calcula a mediana das amostras de RGB.

        A quantidade de amostras é definida pelo parâmetro QUANT_AMOSTRAS_RGB.
        A quantidade de amostras válidas é definida pelo parâmetro PORCENTAGEM_DE_AMOSTRAS_COR_VALIDAS.

        :return: Tupla com a média da mediana das componentes RGB (R, G, B).
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

    @autoSalvarHistoricoDeCor 
    def getColorAdvanced(self):
        # type: () -> Cor
        """
        Determina a cor mais próxima com base na média das amostras de RGB.

        Compara os valores RGB obtidos com valores pré-definidos para identificar a cor mais próxima.

        :return: Cor mais próxima (objeto Cor).
        """
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
        # type: (Cor) -> None
        """
        Adiciona a cor ao histórico de cores.

        :param cor: Cor a ser adicionada (objeto Cor).
        """
        corDiferente = cor != self._historicoCorUnico[0]
        
        for i in range(4, -1, -1):
            if i == 0:
                self._historicoCor[i] = cor
                if corDiferente:
                    self._historicoCorUnico[i] = cor
                break
            
            self._historicoCor[i] = self._historicoCor[i - 1]
            if corDiferente:
                self._historicoCorUnico[i] = self._historicoCorUnico[i - 1]

    def getHistorico(self):
        # type: () -> tuple[Cor, Cor, Cor, Cor, Cor]
        """
        Obtém uma cópia do histórico das últimas cinco cores detectadas.

        :return: Cópia do histórico de cores (tuple de objetos Cor).
        """
        copia = [x for x in self._historicoCor]
        return copia
    
    def getHistoricoUnico(self):
        # type: () -> tuple[Cor, Cor, Cor, Cor, Cor]
        """
        Obtém uma cópia do histórico das últimas cinco cores únicas detectadas.

        :return: Cópia do histórico de cores únicas (tuple de objetos Cor).
        """
        copia = [x for x in self._historicoCorUnico]
        return copia
    
    def setAutoSalvarHistorico(self, salvarHistorico):
        # type: (bool) -> None
        """
        Define se o histórico de cores deve ser salvo automaticamente.

        :param salvarHistorico: True para habilitar o salvamento automático, False para desabilitar.
        """
        self._autoSalvarHistorico = salvarHistorico
        
    def resetarHistorico(self):
        # type: () -> None
        """
        Reseta o histórico de cores para o estado inicial.
        """
        self._historicoCor = [Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE]
        self._historicoCorUnico = [Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE, Cor.NONE]
