from pybricks.robotics import DriveBase  # type: ignore
from FireWall.dispositivos.motor import Motor
from FireWall.dispositivos.sensorGiroscopio import SensorGiroscopio
from FireWall.servicos.servicoDefault import ServicoDefault
from FireWall.enums.direcao import Direcao

class ServicoDeMovimento(ServicoDefault):
    def __init__(self, motor_esquerdo, motor_direito, diametro_roda, distancia_eixos):
        #type: (Motor, Motor, float, float, SensorGiroscopio) -> ServicoDeMovimento
        """
        Classe que representa um veículo robótico com duas rodas motorizadas.

        :param motor_esquerdo: O motor que movimenta a roda esquerda.
        :param motor_direito: O motor que movimenta a roda direita.
        :param diametro_roda: O diâmetro das rodas em milímetros.
        :param distancia_eixos: A distância entre os pontos onde ambas as rodas tocam o chão.
        """
        self.RMotor = motor_direito
        self.LMotor = motor_esquerdo
        self.driveBase = DriveBase(motor_esquerdo.toLego(), motor_direito.toLego(), diametro_roda, distancia_eixos)

    def acelerarPorDiantancia(self, distancia):
        #type: (int) -> None
        """
        Move o robô em linha reta por uma distância especificada e então para.

        :param distancia: Distância a ser percorrida em centimetros.
        """
        correcao = 2.3
        self.driveBase.straight(distancia * correcao)

    def girar(self, angulo, direcao= Direcao.SENTIDOHORARIO):
        #type: (int, Direcao) -> None
        """
        Gira o robô em torno de seu eixo por um ângulo especificado e então para.

        :param angulo: O ângulo de rotação em graus.
        """
        if(direcao == Direcao.SENTIDOANTIHORARIO):
            angulo *= -1
            
        self.driveBase.turn(angulo)
        
    def girar360(self, direcao= Direcao.SENTIDOHORARIO):
        #type: (Direcao) -> None
        """
        Gira o robô em torno de seu eixo por 360 graus.
        """
        anguloCorigido = 300
        
        if(direcao == Direcao.SENTIDOANTIHORARIO):
            anguloCorigido *= -1
        self.driveBase.turn(anguloCorigido)
        
    def girar90(self, direcao= Direcao.SENTIDOHORARIO):
        #type: (Direcao) -> None
        """
        Gira o robô em torno de seu eixo por 90 graus.
        """
        anguloCorigido = 75
        
        if(direcao == Direcao.SENTIDOANTIHORARIO):
            anguloCorigido *= -1
            
        self.driveBase.turn(anguloCorigido)
        
    def girar180(self, direcao= Direcao.SENTIDOHORARIO):
        #type: (Direcao) -> None
        """
        Gira o robô em torno de seu eixo por 180 graus.
        """
        anguloCorigido = 150
        
        if(direcao == Direcao.SENTIDOANTIHORARIO):
            anguloCorigido *= -1
        self.driveBase.turn(anguloCorigido)

    def configurar(self, velocidade_reta=None, aceleracao_reta=None, taxa_giro=None, aceleracao_giro=None):
        #type: (float, float, float, float) -> None
        """
        Configura a velocidade e a aceleração utilizadas pelos métodos mover_reta() e girar().

        :param velocidade_reta: Velocidade do robô em mm/s durante a movimentação em linha reta.
        :param aceleracao_reta: Aceleração linear do robô em mm/s².
        :param taxa_giro: Velocidade de giro do robô em graus/s durante a rotação.
        :param aceleracao_giro: Aceleração angular do robô em graus/s².
        :return: Retorna os valores atuais se nenhum argumento for fornecido.
        """
        self.driveBase.settings(velocidade_reta, aceleracao_reta, taxa_giro, aceleracao_giro)

    def acelerar(self, velocidade_movimento, rotacao = 0):
        #type: (float, float) -> None
        """
        Inicia a movimentação do robô com a velocidade e taxa de giro especificadas.

        :param velocidade_movimento: Velocidade do robô em mm/s.
        :param taxa_giro: Taxa de rotação em graus/s.
        """
        self.driveBase.drive(velocidade_movimento, rotacao)

    def parar(self):
        #type: () -> None
        """
        Para o robô, permitindo que os motores girem livremente.
        """
        self.driveBase.stop()

    def getDistancia(self):
        #type: () -> float
        """
        Obtém a distância percorrida estimada.

        :return: A distância percorrida desde o último reset, em milímetros.
        """
        return self.driveBase.distance()

    def getAngulo(self):
        #type: () -> int
        """
        Obtém o ângulo de rotação acumulado estimado.

        :return: O ângulo de rotação desde o último reset, em graus.
        """
        return self.driveBase.angle()

    def getEstado(self):
        #type: () -> tuple[float, float, float, float]
        """
        Obtém o estado atual do robô.

        :return: Uma tupla contendo a distância percorrida, a velocidade de deslocamento, o ângulo de rotação e a taxa de rotação.
        """
        return self.driveBase.state()

    def resetar(self):
        #type: () -> None
        """
        Reseta a distância percorrida e o ângulo para 0.
        """
        
        self.driveBase.reset()