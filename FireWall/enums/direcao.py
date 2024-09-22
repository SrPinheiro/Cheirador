from pybricks.parameters import Direction # type: ignore

class Direcao:
    """Classe que representa a direção de rotação para valores de velocidade ou ângulo positivos.
    
    SENTIDOHORARIO: Direção positiva que faz o motor girar no sentido horário.
    SENTIDOANTIHORARIO: Direção positiva que faz o motor girar no sentido anti-horário.
    """
    
    SENTIDOHORARIO = Direction.CLOCKWISE  # type: Direction
    SENTIDOANTIHORARIO = Direction.COUNTERCLOCKWISE  # type: Direction
