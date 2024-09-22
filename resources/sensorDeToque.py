
from enums.porta import Porta
from pybricks.ev3devices import TouchSensor

class SensorDeToque:
    """
    LEGO® MINDSTORMS® EV3 Touch Sensor.

    :param port: Porta à qual o sensor está conectado.
    """

    def __init__(self, port):
        # type: (Porta) -> TouchSensor
        self.porta = port

    def isPressionado(self):
        # type: () -> bool
        """
        Verifica se o sensor está pressionado.

        :return: True se o sensor estiver pressionado, False se não estiver.
        :rtype: bool
        """

        return TouchSensor.pressed()
