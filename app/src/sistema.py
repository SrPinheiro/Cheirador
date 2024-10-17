from configs.mapa import Mapa
from FireWall.servicos.servicoDeCor import ServicoDeCor
from FireWall.dispositivos.motor import Motor
from FireWall.dispositivos.cerebro import Cerebro
from FireWall.enums.cor import Cor
from FireWall.utils.tempo import Tempo
from FireWall.servicos.servicoDeMovimento import ServicoDeMovimento
from FireWall.enums.botoes import Botao

class Sistema:
    def __init__(self):
        self.cerebro = Cerebro()
        self.RColorService = ServicoDeCor(Mapa.SENSORSUPERIORDIREITO)
        self.LColorService = ServicoDeCor(Mapa.SENSORSUPERIORESQUERDO)
        self.RMotor = Motor(Mapa.MOTORDIREITO)
        self.LMotor = Motor(Mapa.MOTORESQUERDO)
        self.velocidade = 200
        self.temporizador = Tempo()
        self.direcao = ServicoDeMovimento(self.LMotor, self.RMotor,  1.5, 9.5)
        
    def run(self):
        #self.testarGiro()
        self.iniciarSistema()

         
    
    def iniciarSistema(self):
        self.alinharPorCor()
        self.encontrarTrilha() 
        
    def alinharPorCor(self):
        for _ in range(5):
            while True:
                LCor = self.LColorService.getCor()
                RCor = self.RColorService.getCor()
                
                if(LCor != Cor.BRANCO and RCor != Cor.BRANCO):
                    self.RMotor.trancarGiroDoMotor()
                    self.LMotor.trancarGiroDoMotor()
                    break
                else:
                    self.RMotor.acelerar(self.velocidade)
                    self.LMotor.acelerar(self.velocidade)
            
            self.cerebro.tocarBeep()
            LCor = self.LColorService.getCor()
            RCor = self.RColorService.getCor()
            
            self.RMotor.darRe(40)
            self.LMotor.darRe(40)
            
            while(LCor != Cor.BRANCO and RCor != Cor.BRANCO):
                LCor = self.LColorService.getCor()
                RCor = self.RColorService.getCor()
            
            self.cerebro.imprimirTexto(LCor)
            self.cerebro.imprimirTexto(RCor)

            
            self.RMotor.trancarGiroDoMotor()
            self.LMotor.trancarGiroDoMotor()
            
            if(LCor == Cor.BRANCO):
                LBlue = self.LColorService.getRGB()[2]
                RBlue = self.RColorService.getRGB()[2]
                
                self.LMotor.acelerar(80)
                self.RMotor.darRe(40)   
                
                while(abs(max([LBlue - RBlue, RBlue - LBlue]))) > 10:
                    RBlue = self.RColorService.getRGB()[2]
                    LBlue = self.LColorService.getRGB()[2]
                
                    
            elif(RCor == Cor.BRANCO):
                LBlue = self.LColorService.getRGB()[2]
                RBlue = self.RColorService.getRGB()[2]
                
                self.LMotor.darRe(80)
                self.RMotor.acelerar(40)
                    
                
                while(abs(max([LBlue - RBlue, RBlue - LBlue]))) > 10:
                    RBlue = self.RColorService.getRGB()[2]
                    LBlue = self.LColorService.getRGB()[2]

            
            self.RMotor.trancarGiroDoMotor()
            self.LMotor.trancarGiroDoMotor()
            self.direcao.acelerarPorDiantancia(-0.5)
            self.direcao.parar()     

    def encontrarTrilha(self):
        self.direcao.acelerarPorDiantancia(-6.5)
        self.direcao.girar90()
        self.direcao.parar()
        
        self.encontrarAzul()
        
    def encontrarAzul(self):
        Rcolor = self.RColorService.getCor()
        Lcolor = self.LColorService.getCor()
        
        while Rcolor == Cor.BRANCO or Lcolor == Cor.BRANCO:            
            if(Rcolor == Cor.BRANCO and Lcolor == Cor.BRANCO):
                self.LMotor.acelerar(800)
                self.RMotor.acelerar(800)
                
            elif(Rcolor != Cor.BRANCO):
                self.LMotor.acelerar(0)
                self.RMotor.acelerar(800)
                
            elif(Lcolor != Cor.BRANCO):
                self.LMotor.acelerar(800)
                self.RMotor.acelerar(0)
            
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
            self.alinharPorCor()
            self.direcao.girar180()
            self.direcao.parar()
            
            self.encontrarAzul()
                
    def testarGiro(self):
        while True:
            if self.cerebro.isPressionado(Botao.SUPERIOR):
                self.direcao.girar180()
            if self.cerebro.isPressionado(Botao.CENTRO):
                self.direcao.girar90()
            if self.cerebro.isPressionado(Botao.INFERIOR):
                self.direcao.girar360()
        