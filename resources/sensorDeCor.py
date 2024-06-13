from pybricks.ev3devices import ColorSensor
from resources.defaultResource import Resource

class SensorDeCor(Resource):
    def __init__(self, port):
        self.dispositivo = ColorSensor(port)
        self.porta = port
    
    def getCor(self):
        return self.dispositivo.color()
        
    def getLuzAmbiente(self):
        return self.dispositivo.ambient()

    def getReflexao(self):
        return self.dispositivo.reflection()

    def getRGB(self):
        return self.dispositivo.rgb()
