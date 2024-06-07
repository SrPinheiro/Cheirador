from pybricks.ev3devices import ColorSensor

class SensorDeCor:
    def __init__(self, port):
        self.dispositivo = ColorSensor(port)
    
    def cor(self):
        return self.dispositivo.color()
        
    def luz_ambiente(self):
        return self.dispositivo.ambient()

    def reflexao(self):
        return self.dispositivo.reflection()

    def rgb(self):
        return self.dispositivo.rgb()
