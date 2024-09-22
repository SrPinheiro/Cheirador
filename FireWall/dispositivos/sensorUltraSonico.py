from pybricks.ev3devices import UltrasonicSensor # type: ignore
from FireWall.enums import Porta
from FireWall.dispositivos import DispositivoDefault

class SensorUltrassonico(DispositivoDefault):
    """
    LEGO® MINDSTORMS® EV3 Ultrasonic Sensor.

    :param port: Porta à qual o sensor está conectado.
    """

    def __init__(self, port):
        # type: (Porta) -> None
        self.dispositivo = UltrasonicSensor(port)
        self.porta = port

    def distancia(self, silencioso=False):
        # type: (bool) -> int
        """
        Mede a distância entre o sensor e um objeto usando ondas sonoras ultrassônicas.

        :param silencioso: Escolha True para desligar o sensor após medir a distância, 
                           reduzindo a interferência com outros sensores ultrassônicos.
        :return: Distância medida em milímetros.
        :rtype: int
        """
        return self.dispositivo.distance(silent=silencioso)

    def presenca(self):
        # type: () -> bool
        """
        Verifica a presença de outros sensores ultrassônicos detectando sons ultrassônicos.

        :return: True se sons ultrassônicos forem detectados, False se não forem.
        :rtype: bool
        """
        return self.dispositivo.presence()
