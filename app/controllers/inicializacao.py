from app.models.robo import Robo

class Sistema:
    def __init__(self):
        self.robo = Robo()
        self.robo.cerebro.imprimirImagem('./app/images/logo')
        self.robo.andar()
        
    def run(self):
        while True:
            pass
