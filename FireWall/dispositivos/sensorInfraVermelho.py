from pybricks.ev3devices import InfraredSensor # type: ignore
from FireWall.enums.botoes import Botao
from FireWall.enums.porta import Porta
from FireWall.dispositivos.dispositivoDefault import DispositivoDefault

class SensorInfravermelho(DispositivoDefault):
    """
    LEGO® MINDSTORMS® EV3 Infrared Sensor and Beacon.

    :param port: Porta à qual o sensor está conectado.
    """

    def __init__(self, port):
        # type: (Porta) -> SensorInfravermelho
        self.dispositivo = InfraredSensor(port)
        self.porta = port

    def distancia(self):
        # type: () -> int
        """
        Mede a distância relativa entre o sensor e um objeto usando luz infravermelha.

        :return: Distância relativa variando de 0 (mais próximo) a 100 (mais distante).
        :rtype: int
        """
        return self.dispositivo.distance()

    def distancia_controle(self, canal):
        # type: (int) -> tuple[int | None, int | None]
        """
        Mede a distância relativa e o ângulo entre o controle remoto e o sensor infravermelho.

        :param canal: Número do canal do controle remoto.
        :return: Tupla de distância relativa (0 a 100) e ângulo aproximado (-75 a 75 graus),
                 ou (None, None) se nenhum controle remoto for detectado.
        :rtype: tuple[int, int]
        """
        return self.dispositivo.beacon(canal)

    def getBotoes(self, canal):
        # type: (int) -> list[Botao]
        """
        Verifica quais botões do controle remoto infravermelho estão pressionados.

        :param canal: Número do canal do controle remoto.
        :return: Lista de botões pressionados no controle remoto no canal selecionado.
        :rtype: list[Botao]
        """
        return self.dispositivo.buttons(canal)

    def teclado(self):
        # type: () -> list[Botao]
        """
        Verifica quais botões do controle remoto infravermelho estão pressionados.

        Esta função pode detectar independentemente todos os 4 botões de cima/baixo, mas não pode detectar o botão do controle remoto.

        :return: Lista de botões pressionados no controle remoto.
        :rtype: list[Botao]
        """
        return self.dispositivo.keypad()
