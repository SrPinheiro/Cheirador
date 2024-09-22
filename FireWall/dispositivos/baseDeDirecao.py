from pybricks.robotics import DriveBase  # type: ignore
from FireWall.dispositivos import DispositivoDefault

class BaseDeDirecao(DispositivoDefault):
    def __init__(self, motor_esquerdo, motor_direito, diametro_roda, distancia_eixos):
        """
        Classe que representa um veículo robótico com duas rodas motorizadas e uma roda ou rodízio de suporte opcional.

        :param motor_esquerdo: O motor que movimenta a roda esquerda.
        :param motor_direito: O motor que movimenta a roda direita.
        :param diametro_roda: O diâmetro das rodas em milímetros.
        :param distancia_eixos: A distância entre os pontos onde ambas as rodas tocam o chão.
        """
        
        self.driveBase = DriveBase(motor_esquerdo, motor_direito, diametro_roda, distancia_eixos)

    def acelerarPorDiantancia(self, distancia):
        #type: (int) -> None
        """
        Move o robô em linha reta por uma distância especificada e então para.

        :param distancia: Distância a ser percorrida em milímetros.
        """
        self.driveBase.straight(distancia)

    def girar(self, angulo):
        #type: (int) -> None
        """
        Gira o robô em torno de seu eixo por um ângulo especificado e então para.

        :param angulo: O ângulo de rotação em graus.
        """
        self.driveBase.turn(angulo)
        # Lógica para girar o robô

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

    def distancia(self):
        #type: () -> float
        """
        Obtém a distância percorrida estimada.

        :return: A distância percorrida desde o último reset, em milímetros.
        """
        return self.driveBase.distance()

    def angulo(self):
        #type: () -> int
        """
        Obtém o ângulo de rotação acumulado estimado.

        :return: O ângulo de rotação desde o último reset, em graus.
        """
        return self.driveBase.angle()

    def estado(self):
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