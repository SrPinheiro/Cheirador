import math
from configs.parametros import Parametros

class Matematica:
    
    def MedianaPorVetor(vetor):
        vetor.sort()
        comprimento = len(vetor)
        centro = math.floor(comprimento / 2)

        correcao = comprimento % 2
        quantValores = math.floor(comprimento * Parametros.PORCENTAGEM_DE_AMOSTRAS_COR_VALIDAS) / 2
        inicio = math.floor(centro - quantValores)
        fim = math.ceil(centro + quantValores) + correcao

        media = Matematica.MediaPorVetor(vetor[inicio:fim])
        return media
    

    def MediaPorVetor(vetor):
        return sum(vetor) / len(vetor)
    
    def DiferencaPorVetor(vetor1, vetor2):
        diferenca = 0
        for i in range(len(vetor1)):
            try:
                diferenca += abs(vetor1[i] - vetor2[i])
            except:
                continue

        return diferenca