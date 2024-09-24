from configs.mapa import Mapa
from FireWall.servicos.servicoDeCor import ServicoDeCor
from FireWall.dispositivos.motor import Motor
from FireWall.dispositivos.cerebro import Cerebro
from FireWall.enums.cor import Cor
from FireWall.dispositivos.sensorGiroscopio import SensorGiroscopio
from FireWall.utils.tempo import Tempo
from FireWall.servicos.servicoDeGiroscopio import ServicoDeGiroscopio

class Sistema:
    def __init__(self):
        self.cerebro = Cerebro()
        self.RColorService = ServicoDeCor(Mapa.SENSORDIREITO)
        self.LColorService = ServicoDeCor(Mapa.SENSORESQUERDO)
        self.RMotor = Motor(Mapa.MOTORDIREITO)
        self.LMotor = Motor(Mapa.MOTORESQUERDO)
        self.giroscopio = ServicoDeGiroscopio(Mapa.GIROSCOPIO)
        self.velocidade = 200
        self.temporizador = Tempo()
        
    def run(self):
        for _ in range(4):
            self.RMotor.acelerar(self.velocidade)
            self.LMotor.acelerar(self.velocidade)
            
            while True:
                LCor = self.LColorService.getCor()
                RCor = self.RColorService.getCor()
                
                if(LCor != Cor.BRANCO and RCor != Cor.BRANCO):
                    self.alinharPorCor()
                    self.RMotor.acelerarPorTempo(-400, 2, esperar=False)
                    self.LMotor.acelerarPorTempo(-400, 2, esperar=False)
                    break
        
        self.encontrarTrilha()  
                
    def alinharPorCor(self):
        LCor = self.LColorService.getCor()
        RCor = self.RColorService.getCor()
        self.RMotor.trancarGiroDoMotor()
        self.LMotor.trancarGiroDoMotor()
        self.cerebro.tocarBeep()
        
        self.RMotor.darRe(40)
        self.LMotor.darRe(40)
        
        while(LCor != Cor.BRANCO and RCor != Cor.BRANCO):
            LCor = self.LColorService.getCor()
            RCor = self.RColorService.getCor()
            self.cerebro.tocarBeep()

        
        self.RMotor.trancarGiroDoMotor()
        self.LMotor.trancarGiroDoMotor()
        
        if(LCor == Cor.BRANCO):
            LBlue = self.LColorService.getRGB()[2]
            RBlue = self.RColorService.getRGB()[2]
            
            self.RMotor.darRe(80)
            self.LMotor.acelerar(40)
            
            
            while(abs(max([LBlue - RBlue, RBlue - LBlue]))) > 5:
                RBlue = self.RColorService.getRGB()[2]
                LBlue = self.LColorService.getRGB()[2]
                
        elif(RCor == Cor.BRANCO):
            LBlue = self.LColorService.getRGB()[2]
            RBlue = self.RColorService.getRGB()[2]
            
            self.LMotor.darRe(80)
            self.RMotor.acelerar(40)
            
            while(abs(max([LBlue - RBlue, RBlue - LBlue]))) > 5:
                RBlue = self.RColorService.getRGB()[2]
                LBlue = self.LColorService.getRGB()[2]
                
        
        self.RMotor.trancarGiroDoMotor()
        self.LMotor.trancarGiroDoMotor()
        
        self.cerebro.tocarBeep(5)
        

    def encontrarTrilha(self):
        angulo = self.giroscopio.getAngulo()
        
        self.LMotor.acelerar(100)
        self.RMotor.darRe(100)
        
        anguloAtualizado = self.giroscopio.getAngulo()
        while(anguloAtualizado < angulo + 180):
            anguloAtualizado = self.giroscopio.getAngulo()
            
                
        self.LMotor.trancarGiroDoMotor()
        self.RMotor.trancarGiroDoMotor()
        
        anguloAtualizado = self.giroscopio.getAngulo()
        self.cerebro.imprimirTexto(anguloAtualizado-angulo)
        
        self.LMotor.acelerar(300)
        self.RMotor.acelerar(300)
        
        self.temporizador.pausar(4000)
        self.LMotor.trancarGiroDoMotor()
        self.RMotor.trancarGiroDoMotor()
        
        angulo = self.giroscopio.getAngulo()
        self.LMotor.acelerar(100)
        self.RMotor.darRe(100)
        
        anguloAtualizado = self.giroscopio.getAngulo()
        while(anguloAtualizado < angulo + 90):
            anguloAtualizado = self.giroscopio.getAngulo()
            
        
        self.LMotor.trancarGiroDoMotor()
        self.RMotor.trancarGiroDoMotor()
        
        anguloAtualizado = self.giroscopio.getAngulo()
        self.cerebro.imprimirTexto(anguloAtualizado-angulo)
        
        self.encontrarAzul()
        
    def encontrarAzul(self):
        self.LMotor.acelerar(400)
        self.RMotor.acelerar(400)
        
        Rcolor = self.RColorService.getCor()
        Lcolor = self.LColorService.getCor()
        
        while Rcolor == Cor.BRANCO or Lcolor == Cor.BRANCO:
            Rcolor = self.RColorService.getCor()
            Lcolor = self.LColorService.getCor()
        
        self.LMotor.trancarGiroDoMotor()
        self.RMotor.trancarGiroDoMotor()
        
        RcorAdvanced = self.RColorService.getColorAdvanced()
        LcorAdvanced = self.LColorService.getColorAdvanced()
        
        self.cerebro.imprimirTexto(RcorAdvanced)
        self.cerebro.imprimirTexto(LcorAdvanced)
        
        if(RcorAdvanced == Cor.AZUL and LcorAdvanced == Cor.AZUL):
            while True:
                self.cerebro.tocarBeep()
        else:
            for _ in range(4):
                self.alinharPorCor()
                self.LMotor.trancarGiroDoMotor()
                self.RMotor.trancarGiroDoMotor()
                
            angulo = self.giroscopio.getAngulo()
        
            self.LMotor.acelerar(100)
            self.RMotor.darRe(100)
            
            while(self.giroscopio.getAngulo() < angulo + 175):
                pass
            
            self.LMotor.trancarGiroDoMotor()
            self.RMotor.trancarGiroDoMotor()
            
            self.encontrarAzul()
                
        
        
        
        
        
        
        