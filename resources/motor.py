from pybricks.ev3devices import Motor as MotorLego
from enums.parada import Parada
from enums.direcao import Direcao
from resources.defaultResource import Resource
from enums.porta import Porta

class Motor(Resource):
    """
    LEGO® MINDSTORMS® EV3 Motor.

    Parameters:
        porta (Porta): Porta à qual o motor está conectado.
        direcao_positiva (Direction): Direção em que o motor deve girar quando você fornece um valor de velocidade ou ângulo positivo.
        engrenagens (list): Lista de engrenagens ligadas ao motor.
                      Por exemplo: [12, 36] representa uma engrenagem com 12 dentes e uma com 36 dentes.
                      Use uma lista de listas para múltiplos conjuntos de engrenagens, como [[12, 36], [20, 16, 40]].
    """

    def __init__(self, porta, direcao_positiva=Direcao.SENTIDOHORARIO, engrenagens=None):
        # type: (Porta, Direcao, list) -> None
        self.dispositivo = MotorLego(porta, direcao_positiva, engrenagens)
        self.porta = porta

    def getVelocidade(self):
        # type: () -> int
        """
        Obtém a velocidade do motor.

        Returns:
            int: Velocidade do motor em graus por segundo.
        """
        return self.dispositivo.speed()
    
    def getAngulo(self):
        # type: () -> int
        """
        Obtém o ângulo de rotação do motor.

        Returns:
            int: Ângulo do motor em graus.
        """
        return self.dispositivo.angle()
    
    def resetarAngulo(self, angulo=0):
        # type: (int) -> None
        """
        Define o ângulo acumulado de rotação do motor para um valor desejado.

        Parameters:
            angulo (int): Valor para o qual o ângulo deve ser redefinido.
        """
        self.dispositivo.reset_angle(angulo)

    def ativarNeutro(self):
        # type: () -> None
        """
        Para o motor e permite que ele gire livremente. 
        O motor para gradualmente devido ao atrito.
        """
        self.dispositivo.stop()
    
    def freioDoMotor(self):
        # type: () -> None
        """
        Freia passivamente o motor.
        O motor para devido ao atrito e à voltagem gerada enquanto o motor ainda está se movendo.
        """
        self.dispositivo.brake()

    def trancarGiroDoMotor(self):
        # type: () -> None
        """
        Para o motor e o mantém na posição atual.
        """
        self.dispositivo.hold()

    def acelerar(self, velocidade):
        # type: (int) -> None
        """
        Executa o motor a uma velocidade constante para frente.

        Parameters:
            velocidade (int): Velocidade do motor em graus por segundo.
        """
        if velocidade > 0:
            self.dispositivo.run(velocidade)
        else:
            self.dispositivo.run(0)
        
    def darRe(self, velocidade):
        # type: (int) -> None
        """
        Executa o motor a uma velocidade constante para tras.

        Parameters:
            velocidade (int): Velocidade do motor em graus por segundo.
        """
        if velocidade < 0:
            self.dispositivo.run(velocidade)
        else:
            self.dispositivo.run(0)
        
    def acelerarBidirecional(self, velocidade):
        # type: (int) -> None
        """
        acelera o motor a uma velocidade constante.
        Velocidade positiva = para frente.
        Velocidade negativa = para tras.

        Parameters:
            velocidade (int): Velocidade do motor em graus por segundo.
        """
        self.dispositivo.run(velocidade)

    def acelerarPorTempo(self, velocidade, tempo, entao=Parada.PARAR, esperar=True):
        # type: (int, int, Parada, bool) -> None
        """
        Executa o motor a uma velocidade constante por um tempo determinado.

        Parameters:
            velocidade (int): Velocidade do motor em graus por segundo.
            tempo (int): Duração da manobra em milissegundos.
            entao (Parada): Ação a ser realizada após a parada.
            esperar (bool): Espera pela conclusão da manobra antes de continuar.
        """
        self.dispositivo.run_time(velocidade, tempo, entao, esperar)

    def acelerarPorAngulo(self, velocidade, angulo, entao=Parada.PARAR, esperar=True):
        # type: (int, int, Parada, bool) -> None
        """
        Executa o motor a uma velocidade constante por um ângulo determinado.

        Parameters:
            velocidade (int): Velocidade do motor em graus por segundo.
            angulo (int): Ângulo em que o motor deve rotacionar.
            entao (Parada): Ação a ser realizada após a parada.
            esperar (bool): Espera pela conclusão da manobra antes de continuar.
        """
        self.dispositivo.run_target(velocidade, angulo, entao, esperar)

    def acelerarAteParar(self, velocidade, entao=Parada.PARAR, limite=None):
        # type: (int, Parada, int) -> int
        """
        Executa o motor a uma velocidade constante até que ele pare.

        Parameters:
            velocidade (int): Velocidade do motor em graus por segundo.
            entao (Parada): Ação a ser realizada após a parada.
            limite (int): Limite de torque durante este comando.
        
        Returns:
            int: Ângulo em que o motor se torna bloqueado.
        """
        return self.dispositivo.run_until_stalled(velocidade, entao, limite)

    def rotacionar(self, taxa):
        # type: (float) -> None
        """
        Rotaciona o motor a um ciclo de trabalho dado.

        Parameters:
            taxa (float): Ciclo de trabalho (-100.0 a 100).
        """
        self.dispositivo.dc(taxa)
