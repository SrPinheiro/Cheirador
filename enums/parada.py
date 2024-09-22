from pybricks.parameters import Stop

class Parada:
    """Classe que representa as ações após a parada do motor.

    SOLTAR: Permite que o motor se mova livremente. Ideal para deixar o motor girar sem resistência.
    
    FREIOMOTOR: Resiste passivamente a pequenas forças externas. O motor para gradualmente.
    
    PARAR: Controla ativamente o motor para mantê-lo na posição atual. Disponível apenas em motores com encoders.
    """
    
    SOLTAR = Stop.COAST  # type: Parada
    FREIOMOTOR = Stop.BRAKE  # type: Parada
    PARAR = Stop.HOLD  # type: Parada
