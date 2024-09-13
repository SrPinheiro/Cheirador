from calibrators.defaultCalibrator import Calibrador
from resources.cerebro import Cerebro
from app.services.colorService import ColorService
from configs.mapa import Mapa
from utils.tempo import Tempo
from enums.botoes import Botao

class CalibradorDeCor(Calibrador):

    def __init__(self):
        self.cerebro = Cerebro()
        self.colorService = ColorService(Mapa.SENSORDIREITO)

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
        

