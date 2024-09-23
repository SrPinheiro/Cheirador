from FireWall.configs import Parametros
import math

class Matematica:
    
    @staticmethod
    def MedianaPorVetor(vetor, amostrasValidas = Parametros.PORCENTAGEM_DE_AMOSTRAS_COR_VALIDAS):
        # type: (list[int | float], float) -> float
        vetor.sort()
        comprimento = len(vetor)
        centro = math.floor(comprimento / 2)

        correcao = comprimento % 2
        quantValores = math.floor(comprimento * amostrasValidas) / 2
        inicio = math.floor(centro - quantValores)
        fim = math.ceil(centro + quantValores) + correcao

        media = Matematica.MediaPorVetor(vetor[inicio:fim])
        return media
    
    @staticmethod
    def MediaPorVetor(vetor):
        #type: (list[int | float]) -> float
        resultado = (sum(vetor) / len(vetor)) if len(vetor) != 0 else 0.0
        return resultado
    
    @staticmethod
    def DiferencaPorVetor(vetor1, vetor2):
        #type: (list[int | float], list[int | float]) -> float
        diferenca = 0
        for i in range(len(vetor1)):
            try:
                diferenca += abs(vetor1[i] - vetor2[i])
            except:
                continue

        return diferenca