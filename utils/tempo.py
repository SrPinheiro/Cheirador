from pybricks.tools import wait, StopWatch

class Tempo:
    """
    Classe para controlar pausas e manipular um cronômetro.

    Métodos:
        pausar: Pausa o programa por um tempo especificado.
        getCronometro: Retorna o tempo decorrido do cronômetro.
        pausarCronometro: Pausa o cronômetro.
        retomarCronometro: Retoma o cronômetro.
        resetarCronometro: Reseta o cronômetro para zero.
    """

    def __init__(self):
        pass  # type: () -> None

    def pausar(self, tempo):
        # type: (int) -> None
        """
        Pausa o programa por um tempo especificado.

        Parameters:
            tempo (int): Tempo em milissegundos para esperar.
        """
        wait(tempo)  

    def getCronometro(self):
         # type: () -> int
        """
        Retorna o tempo decorrido do cronômetro.

        Returns:
            int: Tempo decorrido em milissegundos.
        """
        return StopWatch.time() 

    def pausarCronometro(self):
         # type: () -> None
        """
        Pausa o cronômetro.
        """
        StopWatch.pause()

    def retomarCronometro(self):
        # type: () -> None
        """
        Retoma o cronômetro.
        """
        StopWatch.resume() 

    def resetarCronometro(self):
        # type: () -> None
        """
        Reseta o cronômetro para zero.
        """
        StopWatch.reset()  
