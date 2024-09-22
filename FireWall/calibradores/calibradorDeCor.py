from utils.tempo import Tempo
from FireWall.enums import Botao, Porta
from FireWall.services import ColorService
from FireWall.dispositivos import Cerebro
from FireWall.calibradores import CalibradorDefault

class CalibradorDeCor(CalibradorDefault):

    def __init__(self, porta):
        #type: (Porta) -> CalibradorDeCor
        self.cerebro = Cerebro()
        self.colorService = ColorService(porta)

    def run(self):
        cores = ['verde', 'preto', 'azul', 'marrom', 'amarelo', 'branco', 'vermelho']
        dados = { }
        for cor in cores:
            while True:
                self.cerebro.imprimirTexto("Cor: {}".format(cor))
                COR = self.colorService.getRGB()
                self.cerebro.imprimirTexto(COR)

                Tempo.pausar(1000)
                self.cerebro.limparTela()

                if(self.cerebro.isPressionado(Botao.CENTRO)):
                    dados[cor] = COR
                    break
                    
                
        while(True):
            self.cerebro.limparTela()
        

