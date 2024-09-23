from FireWall.servicos import ServicoDefault
from FireWall.enums import Porta
from FireWall.dispositivos import SensorUltraSonico
from FireWall.helpers import Matematica, autoSalvarHistoricoDeDistancia

class ServicoUltrasonico(ServicoDefault):
    """
    * Classe com servicos uteis para o sensor ultrasonico.
    """
    
    def __init__(self, porta, salvarHistorico = True):
        #type: (Porta, bool) -> ServicoUltrasonico
        self.ultrasonico = SensorUltraSonico(porta)
        self._historico = [None, None, None, None, None] #type: list[float | None]
        self._autoSalvar = salvarHistorico
        
    @autoSalvarHistoricoDeDistancia
    def getDistancia(self):
        #type: () -> float
        amostras = [] #type: list[int]
        
        for _ in range(10):
            distancia = self.ultrasonico.distancia()
            amostras.append(distancia)
            
        resultado = Matematica.MedianaPorVetor(amostras, 0.5)
        
        return resultado
    
    def getHistorico(self):
        #type: () -> tuple[float, float, float, float, float]
        copiaHistorico = [x for x in self._historico]
        return copiaHistorico
    
    def adicionarDistanciaNoHistorico(self, distancia):
        #type: (float) -> None
        for i in range(4, -1, -1):
            if(i == 0):
                self._historico[i] = distancia
                break
            self._historico[i] = self._historico[i -1]
            
    def limparHistorico(self):
        #type: () -> None
        self._historico = [None, None, None, None, None]