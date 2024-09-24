from pybricks.ev3devices import GyroSensor # type: ignore
from FireWall.enums.direcao import Direcao
from FireWall.enums.porta import Porta
from FireWall.dispositivos.dispositivoDefault import DispositivoDefault

class SensorGiroscopio(DispositivoDefault):
    """
    LEGO® MINDSTORMS® EV3 Gyro Sensor.

    Parameters:
        porta (Porta): Porta à qual o sensor está conectado.
        direcao_positiva (Direction): Direção de rotação positiva ao olhar para o ponto vermelho no topo do sensor.
    """

    def __init__(self, porta, direcao_positiva=Direcao.SENTIDOHORARIO):
        # type: (Porta, Direcao) -> None
        self.dispositivo = GyroSensor(porta, direcao_positiva)
        self.porta = porta

    def getVelocidade(self):
        # type: () -> int
        """
        Obtém a velocidade (velocidade angular) do sensor.

        Returns:
            int: Velocidade angular do sensor em graus por segundo.
        """
        return self.dispositivo.speed()

    def getAngulo(self):
        # type: () -> int
        """
        Obtém o ângulo acumulado do sensor.

        Returns:
            int: Ângulo de rotação em graus.
        
        Note:
            Se você usar o método angulo(), não pode usar o método velocidade() no mesmo programa, 
            pois isso redefinirá o ângulo do sensor para zero toda vez que você ler a velocidade.
        """
        return self.dispositivo.angle()

    def resetar_angulo(self, angulo=0):
        # type: (int) -> None
        """
        Define o ângulo de rotação do sensor para um valor desejado.

        Parameters:
            angulo (int): Valor para o qual o ângulo deve ser redefinido. O padrão é 0.
        """
        self.dispositivo.reset_angle(angulo)
