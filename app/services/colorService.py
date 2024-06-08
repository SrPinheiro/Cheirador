from resources.sensorDeCor import SensorDeCor
from app.services.defaultService import Service

class ColorService(Service):
    def __init__(self, porta):
        self.dispositivo = SensorDeCor(porta)

    def getColor(self):
        return self.dispositivo.getCor()