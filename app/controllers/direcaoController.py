from app.controllers.controladorDefault import ControladorDefault
from FireWall.enums.cor import Cor
from FireWall.servicos.servicoDeCor import ServicoDeCor
from FireWall.dispositivos.motor import Motor
from FireWall.servicos.servicoDeMovimento import ServicoDeMovimento
from FireWall.dispositivos.cerebro import Cerebro

class DirecaoController(ControladorDefault):
    
    def __init__(self, cerebro, sensorDeCorEsquerdo, SensorDeCorDireito, motorEsquerdo, motorDireito, direcao):
        #type: (Cerebro, ServicoDeCor, ServicoDeCor, Motor, Motor, ServicoDeMovimento ) -> DirecaoController
        self.RColorService = sensorDeCorEsquerdo
        self.LColorService =SensorDeCorDireito
        self.LMotor = motorEsquerdo
        self.RMotor = motorDireito
        self.direcao = direcao
        self.cerebro = cerebro
        self.velocidade = 200
        
    
    def alinhar_com_a_linha(self):
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
        
        self.cerebro.tocarBeep(5)
        