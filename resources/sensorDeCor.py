from pybricks.ev3devices import ColorSensor
from resources.defaultResource import Resource
from enums.cor import Cor
from enums.porta import Porta

class SensorDeCor(Resource):
    """
    LEGO® MINDSTORMS® EV3 Color Sensor.

    :param porta: Porta à qual o sensor está conectado.
    """

    def __init__(self, porta):
        # type: (Porta) -> Cor
        self.dispositivo = ColorSensor(porta)
        self.porta = porta
    
    def getCor(self):
        # type: () -> Cor
        """
        Mede a cor de uma superfície.

        :return: Cor detectada, que pode ser Color.BLACK, Color.BLUE, Color.GREEN,
                 Color.YELLOW, Color.RED, Color.WHITE, Color.BROWN ou None se nenhuma cor
                 for detectada.
        :rtype: Cor
        """
        return self.dispositivo.color()
        
    def getLuzAmbiente(self):
        # type: () -> int
        """
        Mede a intensidade da luz ambiente.

        :return: Intensidade da luz ambiente, variando de 0 (escuro) a 100 (brilhante).
        :rtype: int
        """
        return self.dispositivo.ambient()

    def getReflexao(self):
        # type: () -> int
        """
        Mede a reflexão de uma superfície usando luz vermelha.

        :return: Reflexão, variando de 0 (sem reflexão) a 100 (alta reflexão).
        :rtype: int
        """
        return self.dispositivo.reflection()

    def getRGB(self):
        # type: () -> tuple[int, int, int]
        """
        Mede a reflexão de uma superfície usando luz vermelha, verde e azul.

        :return: Tupla de reflexões para luz vermelha, verde e azul, cada uma variando de
                 0.0 (sem reflexão) a 100.0 (alta reflexão).
        :rtype: list[int]
        """
        return self.dispositivo.rgb()
